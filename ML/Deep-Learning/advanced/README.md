# 🧠 Deep Learning — ADVANCED

### *Modern architectures and training paradigms beyond basic CNN/AE*

> **Nav:** [← DL Theory (basics)](../ml_dl_cnn_ae_theory.md) | [← ML Master Index](../../ml_master_gap_index.md) | [← Neural Networks Advanced](../../Neural-Networks/advanced/README.md)

---

## 📚 Contents of this folder

| # | File | Topics |
|---|---|---|
| 1 | [ml_dl_adv_rnn_lstm_gru.md](ml_dl_adv_rnn_lstm_gru.md) | Vanilla RNN, LSTM gates, GRU, bidirectional, seq2seq, teacher forcing |
| 2 | [ml_dl_adv_transformers.md](ml_dl_adv_transformers.md) | Self-attention, multi-head, positional encoding, encoder/decoder, masking, complexity |
| 3 | [ml_dl_adv_generative.md](ml_dl_adv_generative.md) | Variational Autoencoders, GAN (DCGAN, WGAN, WGAN-GP), quick Diffusion intuition |
| 4 | [ml_dl_adv_modern_cnns.md](ml_dl_adv_modern_cnns.md) | ResNet, DenseNet, MobileNet, EfficientNet, Vision Transformer (ViT), ConvNeXt |
| 5 | [ml_dl_adv_transfer_tricks.md](ml_dl_adv_transfer_tricks.md) | Transfer learning, fine-tuning recipes, LR schedules, warmup, mixed precision, data augmentation (mixup/cutmix), gradient accumulation, distributed training basics |

---

## 🧭 Reading order

Read them in the order above for a linear narrative: sequence models → attention → generative → modern CNNs → how to train all of them.

---

## 🔗 Prerequisites

- **CNN + autoencoder** basics from [DL theory basics](../ml_dl_cnn_ae_theory.md)
- **Backprop** from [NN theory basics](../../Neural-Networks/ml_nn_mlp_bp_theory.md)
- Everything in [NN advanced](../../Neural-Networks/advanced/README.md) — optimizers, regularization, gradients

---

## 🎯 What you'll know after reading

- How LSTMs solve the vanishing-gradient problem in sequence models and why they've been largely replaced by transformers
- The exact shape of self-attention and why the complexity is O(n²)
- The difference between VAE and GAN and what a likelihood-free model actually is
- Why ResNet-50 is still a reasonable baseline in 2026 even though ViT exists
- How to fine-tune a pretrained model without destroying the pretrained features

---

> *ML · Deep Learning Advanced · github.com/rpaut03l/TS-01*
