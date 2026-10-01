from pathlib import Path
import matplotlib.pyplot as plt

from surgicalvision3d.data.synthetic import synthetic_laparoscopic_frame, synthetic_depth_surface


def main() -> None:
    out=Path("outputs/demo_assets"); out.mkdir(parents=True,exist_ok=True)
    frame=synthetic_laparoscopic_frame()
    depth=synthetic_depth_surface()
    plt.imsave(out/"synthetic_laparoscopic_frame.png",frame)
    plt.imsave(out/"synthetic_depth.png",depth,cmap="viridis")
    print(f"wrote demo assets to {out}")


if __name__ == "__main__":
    main()
