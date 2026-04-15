# 📖 DL Advanced: Generative Models — VAE · GAN · Diffusion

### *Likelihood-based (VAE) · adversarial (GAN) · score-based (Diffusion)*

> **Nav:** [← Transformers](ml_dl_adv_transformers.md) | [advanced README](README.md) | [Modern CNNs →](ml_dl_adv_modern_cnns.md)

---

## 🧠 MNEMONIC: **"VGWD"**

> **V**AE · **G**AN · **W**asserstein · **D**iffusion

---

## 📚 Table of Contents

| # | Topic | Jump |
|---|-------|------|
| 1 | What Generative Models Do | [§1](#1-what-generative-models-do) |
| 2 | Variational Autoencoders (VAE) | [§2](#2-variational-autoencoders-vae) |
| 3 | The ELBO | [§3](#3-the-elbo) |
| 4 | The Reparameterization Trick | [§4](#4-the-reparameterization-trick) |
| 5 | Generative Adversarial Networks (GAN) | [§5](#5-generative-adversarial-networks-gan) |
| 6 | Training Instabilities & Mode Collapse | [§6](#6-training-instabilities--mode-collapse) |
| 7 | Wasserstein GAN (WGAN / WGAN-GP) | [§7](#7-wasserstein-gan) |
| 8 | Conditional & DCGAN | [§8](#8-conditional--dcgan) |
| 9 | Diffusion Models (quick take) | [§9](#9-diffusion-models) |
| 10 | VAE vs GAN vs Diffusion | [§10](#10-vae-vs-gan-vs-diffusion) |
| 11 | Cheat Sheet | [§11](#11-cheat-sheet--exam-hacks) |

---

## 1. What Generative Models Do

They learn a distribution **p(x)** over data such that you can:
1. **Sample** new instances from it — generate a fake face, fake audio, fake text.
2. **Evaluate** probabilities — compute p(x) for a given x (density estimation).
3. **Manipulate** — interpolate, edit, condition on labels or text.

Three main approaches differ in how much of (1), (2), (3) they support:
- **Autoregressive (GPT-style):** all three, but slow sampling.
- **VAE:** all three, lower sample quality.
- **GAN:** sampling only, highest sample quality historically.
- **Diffusion:** sampling + some editing, current state of the art.
- **Flow-based:** exact likelihood, lower sample quality.

[↑ Back to Top](#-dl-advanced-generative-models--vae--gan--diffusion)

---

## 2. Variational Autoencoders (VAE)

Kingma & Welling (2013). A probabilistic autoencoder with a regularized latent space.

### Architecture
```
ENCODER q_φ(z|x) outputs  μ(x), σ(x)  (parameters of a Gaussian)
                 z ~ N(μ(x), σ²(x))
DECODER p_θ(x|z) reconstructs x from z
```

### Training objective (ELBO)
```
L(θ, φ; x) = E_{q(z|x)} [ log p(x|z) ]  −  KL( q(z|x) ‖ p(z) )
             ↓                            ↓
         reconstruction              regularization (KL to prior)
```

- **p(z)** is usually **N(0, I)** — a standard Gaussian prior.
- We maximize the ELBO (evidence lower bound), which lower-bounds log p(x).

### Intuition
- **Reconstruction term** makes decoder outputs resemble x.
- **KL term** keeps z's posterior close to N(0, I) so you can sample new z from the prior and decode them into novel x.

[↑ Back to Top](#-dl-advanced-generative-models--vae--gan--diffusion)

---

## 3. The ELBO

For any q_φ(z|x):
```
log p(x) = E_{q} [ log p(x|z) ] − KL(q(z|x) ‖ p(z)) + KL(q(z|x) ‖ p(z|x))
         ≥ E_{q} [ log p(x|z) ] − KL(q(z|x) ‖ p(z))         (last term ≥ 0)
         = ELBO
```

### KL term in closed form (Gaussian vs Gaussian)
For q = N(μ, diag(σ²)) and p = N(0, I):
```
KL = ½ Σ_k ( μ_k² + σ_k² − log σ_k² − 1 )
```
No Monte Carlo needed.

### Reconstruction term
```
L_rec = Σ_i ‖ x_i − x̂_i ‖²       (Gaussian likelihood)
or
L_rec = BCE(x, x̂)                 (Bernoulli likelihood, binarized MNIST)
```

[↑ Back to Top](#-dl-advanced-generative-models--vae--gan--diffusion)

---

## 4. The Reparameterization Trick

Sampling **z ~ N(μ, σ²)** is not differentiable with respect to μ, σ — you can't backprop through random sampling.

### The trick
```
ε ~ N(0, I)
z = μ + σ · ε
```
Now z is a **deterministic function of the parameters + fixed noise ε**. Gradients flow through μ and σ cleanly. The stochasticity lives in ε, which has no trainable parameters.

This single idea is what makes VAE training practical.

[↑ Back to Top](#-dl-advanced-generative-models--vae--gan--diffusion)

---

## 5. Generative Adversarial Networks (GAN)

Goodfellow et al. (2014). Train two networks in competition.

### The setup
- **Generator** G(z) — maps a random noise vector z to a fake sample.
- **Discriminator** D(x) — tries to tell real from fake.

### The objective
```
min_G max_D  E_{x~p_data} [log D(x)]  +  E_{z~p_z} [log(1 − D(G(z)))]
```

- D tries to **maximize** its classification ability.
- G tries to **minimize** D's ability (i.e., fool it).
- At equilibrium, **G matches p_data** and **D is everywhere 0.5**.

### Training loop (one step)
```
1. Sample minibatch x_real from data.
2. Sample z, generate x_fake = G(z).
3. Update D to classify real vs fake correctly.
4. Update G to make D think the fakes are real.
   (usually 1 D step : 1 G step, sometimes 5:1)
```

[↑ Back to Top](#-dl-advanced-generative-models--vae--gan--diffusion)

---

## 6. Training Instabilities & Mode Collapse

GANs are notoriously fragile.

### Vanishing gradients
When D becomes too good, its gradient for G vanishes (`log(1 − D(G(z)))` saturates → 0). Fix: use the **non-saturating** loss `−log D(G(z))` for G instead.

### Mode collapse
G figures out that one or two kinds of outputs reliably fool D → it stops producing diverse samples. You get 100 identical faces.

**Fixes:**
- **Minibatch discrimination** (Salimans et al. 2016).
- **Historical averaging.**
- **Wasserstein GAN** (see next section).

### Balance problem
If D wins (too accurate), G has no gradient. If G wins, D has no signal. Getting the ratio right is an art.

[↑ Back to Top](#-dl-advanced-generative-models--vae--gan--diffusion)

---

## 7. Wasserstein GAN

Arjovsky et al. (2017). Replace the Jensen-Shannon divergence of vanilla GAN with the **Wasserstein-1** (Earth Mover's) distance:

```
W(p_r, p_g) = sup_{‖f‖_L ≤ 1}  E_{x~p_r}[f(x)] − E_{x~p_g}[f(x)]
```

### Why it's better
- **Never vanishing gradient** even when D (now called the "critic") is much better than G.
- **Mode collapse reduced.**
- **Loss correlates with sample quality** — you can actually trust the loss curve.

### The Lipschitz constraint
The critic f must be 1-Lipschitz. Original WGAN enforced this with **weight clipping** (ugly). **WGAN-GP** (Gulrajani 2017) enforces it with a **gradient penalty** — train-time penalty pushing ‖∇f‖ → 1 at random interpolation points. This is the standard version.

```
L_D = E_{x_fake}[D(x_fake)] − E_{x_real}[D(x_real)]
      + λ · E_{x̂} [(‖∇_x̂ D(x̂)‖ − 1)²]      (gradient penalty)
L_G = −E_{x_fake}[D(x_fake)]
```

[↑ Back to Top](#-dl-advanced-generative-models--vae--gan--diffusion)

---

## 8. Conditional & DCGAN

### Conditional GAN (cGAN)
Add a class label y as input to both G and D:
```
G(z, y)    D(x, y)
```
Now you can generate "a 7" vs "a 3". Image-to-image translation (pix2pix, CycleGAN) is built on this idea.

### DCGAN
Radford et al. (2015). A set of practical tricks that made GANs work reliably on images:
- **Convolutional** generator and discriminator (strided conv / transposed conv for up-sampling).
- **BatchNorm** in both (except output layer of G and input layer of D).
- **LeakyReLU** in D (slope 0.2).
- **Tanh** at the generator output; images scaled to [−1, 1].
- **Adam** with lr = 2e−4, β₁ = 0.5.

DCGAN became the standard recipe that most subsequent image GANs built on.

[↑ Back to Top](#-dl-advanced-generative-models--vae--gan--diffusion)

---

## 9. Diffusion Models

Sohl-Dickstein et al. (2015), Ho et al. (2020). The current state of the art for image, audio, and video generation.

### The idea
**Forward process:** gradually add Gaussian noise to a data sample over T steps until it becomes pure noise.
```
x_0 → x_1 → x_2 → ... → x_T ≈ N(0, I)
```

**Reverse process:** train a neural network to **denoise** one step at a time, starting from pure noise and ending at a clean sample.

### Training objective (DDPM)
Very simple, surprisingly:
```
L = E_{x_0, t, ε} [ ‖ ε − ε_θ(x_t, t) ‖² ]
```
where `x_t = √(ᾱ_t) · x_0 + √(1 − ᾱ_t) · ε` is a **noisy version** of x_0. The network ε_θ just has to **predict the noise** that was added.

### Sampling
Start from x_T ~ N(0, I) and iteratively apply the learned reverse step. Takes many (e.g., 50-1000) steps per sample — the main drawback.

### Why diffusion beat GANs
- **Stable training** — no adversarial game, no mode collapse.
- **Easy to scale.**
- **Great sample diversity.**
- **Trainable on vast unlabeled data.**
- **Classifier-free guidance** gives an easy quality/diversity knob.

### Fast sampling
DDIM, DPM++, etc. let you sample in ~10-50 steps instead of 1000. **Consistency models** (Song et al. 2023) push toward single-step sampling.

[↑ Back to Top](#-dl-advanced-generative-models--vae--gan--diffusion)

---

## 10. VAE vs GAN vs Diffusion

```
┌─────────────┬───────────┬──────────┬────────────┐
│             │ VAE       │ GAN      │ DIFFUSION  │
├─────────────┼───────────┼──────────┼────────────┤
│ Likelihood  │ ELBO      │ implicit │ ELBO / ... │
│ Training    │ stable    │ unstable │ stable     │
│ Sample qty  │ decent    │best (was)│ best       │
│ Sample div  │ good      │mode coll.│ best       │
│ Sample speed│ fast      │fast      │ slow       │
│ Main use    │ latent ML │GAN era   │ 2022+ SOTA │
└─────────────┴───────────┴──────────┴────────────┘
```

- **VAE** — useful for latent representations, interpretable structure, anomaly detection.
- **GAN** — still the go-to for real-time image generation and some style transfer.
- **Diffusion** — SOTA for image/audio/video quality; backbone of Stable Diffusion, DALL·E 3, Imagen, Sora-style video.

[↑ Back to Top](#-dl-advanced-generative-models--vae--gan--diffusion)

---

## 11. Cheat Sheet & Exam Hacks

```
╔══════════════════════════════════════════════════════════════╗
║  GENERATIVE MODELS ONE-LINERS                                ║
╠══════════════════════════════════════════════════════════════╣
║  VAE: maximize ELBO = recon − KL(q(z|x) ‖ p(z))              ║
║  Reparameterization: z = μ + σ·ε (backprop through sampling) ║
║  GAN: min_G max_D E[log D(x)] + E[log(1 − D(G(z)))]          ║
║  Mode collapse: G produces only a few outputs                ║
║  WGAN-GP: Wasserstein distance + gradient penalty            ║
║  DCGAN: strided conv, BN, LeakyReLU, tanh output             ║
║  Diffusion: predict the noise, denoise step by step          ║
║  Training objective ‖ ε − ε_θ(x_t, t) ‖² is astonishingly    ║
║     simple and works                                         ║
╚══════════════════════════════════════════════════════════════╝
```

### ⚡ Exam Red Flags
1. **"What's the reparameterization trick?"** — writes z = μ + σ·ε so gradients flow through μ, σ while randomness stays in ε.
2. **"Two terms in the ELBO?"** — reconstruction (make decoder fit data) + KL regularization (keep latent near prior).
3. **"Why WGAN?"** — replaces JSD with Wasserstein distance → meaningful gradients even when D is near-perfect, reduces mode collapse.
4. **"DCGAN recipe essentials?"** — strided conv, BN, LeakyReLU (D), tanh (G output), Adam 2e−4 with β₁ = 0.5.
5. **"Diffusion: what does the model actually predict?"** — the noise ε added at step t (equivalently, the clean x_0 or the score function, via reparameterization).
6. **"Why did diffusion beat GANs?"** — stable training, easy to scale, great sample diversity, no mode collapse.

[↑ Back to Top](#-dl-advanced-generative-models--vae--gan--diffusion)

---

### 💻 Quick Code

```python
import torch, torch.nn as nn, torch.nn.functional as F

# VAE — minimal
class VAE(nn.Module):
    def __init__(self, d_in=784, d_z=32):
        super().__init__()
        self.enc = nn.Sequential(nn.Linear(d_in, 256), nn.ReLU(), nn.Linear(256, 2 * d_z))
        self.dec = nn.Sequential(nn.Linear(d_z, 256), nn.ReLU(), nn.Linear(256, d_in), nn.Sigmoid())

    def forward(self, x):
        mu_logvar = self.enc(x)
        mu, logvar = mu_logvar.chunk(2, dim=-1)
        std = (0.5 * logvar).exp()
        eps = torch.randn_like(std)
        z = mu + std * eps                          # reparameterization
        x_hat = self.dec(z)
        return x_hat, mu, logvar

def vae_loss(x, x_hat, mu, logvar):
    recon = F.binary_cross_entropy(x_hat, x, reduction="sum")
    kld = -0.5 * (1 + logvar - mu.pow(2) - logvar.exp()).sum()
    return recon + kld

# DCGAN-style training step (simplified)
def gan_step(G, D, x_real, opt_G, opt_D, bce):
    B = x_real.size(0)
    z = torch.randn(B, 100, 1, 1, device=x_real.device)
    # ---- D step ----
    opt_D.zero_grad()
    d_real = D(x_real)
    d_fake = D(G(z).detach())
    loss_d = bce(d_real, torch.ones_like(d_real)) + bce(d_fake, torch.zeros_like(d_fake))
    loss_d.backward(); opt_D.step()
    # ---- G step ----
    opt_G.zero_grad()
    d_fake = D(G(z))
    loss_g = bce(d_fake, torch.ones_like(d_fake))   # non-saturating
    loss_g.backward(); opt_G.step()
```

---

> **Next:** [Modern CNNs →](ml_dl_adv_modern_cnns.md)
>
> *ML · Deep Learning Advanced · github.com/rpaut03l/TS-01*
