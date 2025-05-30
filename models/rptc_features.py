import torch
import torch.nn.functional as F

def extract_rptc_features(image_batch):
    # image_batch: [B, C, H, W], normalized RGB images
    device = image_batch.device

    # Convert to grayscale
    image_batch = image_batch.mean(dim=1, keepdim=True)  # [B, 1, H, W]
    B, C, H, W = image_batch.shape
    window_size = 5
    pad = window_size // 2

    # Pad image
    padded = F.pad(image_batch, (pad, pad, pad, pad), mode='reflect')  # [B, 1, H+4, W+4]

    # Extract patches using unfold
    patches = padded.unfold(2, window_size, 1).unfold(3, window_size, 1)  # [B, 1, H, W, 5, 5]
    mean_patch = patches.mean(dim=(-1, -2))  # [B, 1, H, W]
    std_patch = patches.std(dim=(-1, -2))    # [B, 1, H, W]

    threshold = std_patch.median(dim=-1, keepdim=True).values.median(dim=-2, keepdim=True).values
    rich_mask = std_patch > threshold
    poor_mask = std_patch <= threshold

    # Compute correlation with shifted versions
    correlation_maps = []
    shifts = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1), (1, 0),  (1, 1)]

    for dy, dx in shifts:
        shifted = F.pad(image_batch, (1, 1, 1, 1), mode='reflect')  # pad for rolling
        shifted = shifted[:, :, 1 + dy : 1 + dy + H, 1 + dx : 1 + dx + W]
        corr = (image_batch * shifted).mean(dim=(1, 2, 3))  # [B]
        correlation_maps.append(corr)

    features = torch.stack(correlation_maps, dim=1)  # [B, 8]
    print("Kullaniliyor")
    return features.to(device)
