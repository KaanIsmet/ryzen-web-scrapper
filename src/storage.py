from pathlib import Path
import pandas as pd
class Storage:
    def __init__(self, base_path="data"):
        self.base_path = Path(base_path)
        self.base_path.mkdir(exist_ok=True)

    def save_to_csv(self, data, filename):
        df = pd.DataFrame(data)
        df.to_csv(self.base_path / f"{filename}.csv", index=False)

    def load_from_csv(self, filename):
        return pd.read_csv(self.base_path / f"{filename}.csv")

