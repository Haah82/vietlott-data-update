#!/usr/bin/env python
"""
README Generator for Vietlott Data Project

This script generates a comprehensive README.md file for the GitHub repository
frontpage, including data statistics and project information.
"""

from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

import polars as pl
from loguru import logger
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import itertools
from collections import Counter

matplotlib.use("Agg")  # For headless environments like GitHub Actions

from vietlott.config.products import get_config


class ReadmeTemplates:
    """Container for README template strings and formatting."""

    @staticmethod
    def get_header() -> str:
        """Get the main header with badges and description."""
        return """# 🎰 Vietlott Data

[![GitHub Actions](https://github.com/haah82/vietlott-data-update/workflows/crawl/badge.svg)](https://github.com/haah82/vietlott-data-update/actions)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Data Updated](https://img.shields.io/badge/data-daily%20updated-brightgreen.svg)](https://github.com/haah82/vietlott-data-update/commits/main)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Deployed-blue)](https://haah82.github.io/vietlott-data-update/)

> 📊 **Thu thập và Tổng hợp Dữ liệu Vietlott Tự động nhằm mục đích học tập và giải trí**
>
> Dự án tự động thu thập và phân tích dữ liệu kết quả xổ số từ [vietlott.vn](https://vietlott.vn/), cung cấp thống kê chi tiết cho tất cả các sản phẩm.

## 🎯 Supported Lottery Products

| Product | Link | Description |
|---------|------|-------------|
| **Power 6/55** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/655.html) | Choose 6 numbers from 1-55 |
| **Power 6/45** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/645.html) | Choose 6 numbers from 1-45 |
| **Power 5/35** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/535.html) | Choose 5 numbers from 1-35 |
| **Keno** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-keno.html) | Fast-pace number game |
| **Max 3D** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/max-3d.html) | 3-digit lottery game |
| **Max 3D Pro** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/max-3dpro.html) | Enhanced 3D lottery |
| **Bingo18** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-bingo18.html) | 3 numbers from 0-9 game |
"""

    @staticmethod
    def get_toc() -> str:
        """Get table of contents."""
        return """## 📋 Table of Contents

- [🎯 Supported Lottery Products](#-supported-lottery-products)
- [Predictions](#-predictions)
- [📊 Data Statistics](#-data-statistics)
- [📈 Power 6/55 Analysis](#-power-655-analysis)
  - [📅 Recent Results](#-recent-results)
  - [🎲 Number Frequency (All Time)](#-number-frequency-all-time)
  - [📊 Frequency Analysis by Period](#-frequency-analysis-by-period)
- [📈 Power 6/45 Analysis](#-power-645-analysis)
  - [📅 Recent Results 6/45](#-recent-results-last-10-draws-645)
  - [🎲 Number Frequency 6/45](#-number-frequency-all-time-645)
- [📈 Max 3D Analysis](#-max-3d-analysis)
- [📈 Max 3D Pro Analysis](#-max-3d-pro-analysis)
- [🏆 Top Probability Summary](#-top-probability-summary)
- [⚙️ How It Works](#️-how-it-works)
- [🚀 Installation & Usage](#-installation--usage)
- [📄 License](#-license)
"""

    @staticmethod
    def get_how_it_works() -> str:
        """Get how it works section."""
        return """## ⚙️ How It Works

### 🤖 Automated Data Collection

This project runs completely automatically using **GitHub Actions** - no server required!

- **⏰ Schedule**: Runs daily via [GitHub Actions workflow](.github/workflows/crawl.yaml)
- **🔄 Process**: Fetches latest results → Processes data → Commits to repository
- **📊 Analysis**: Generates statistics and updates README automatically

### 🕵️ Data Crawling Method

The data collection works by:
1. **🔍 Network Analysis**: Inspecting browser-server communication
2. **🐍 Python Replication**: Recreating the data fetch logic in Python
3. **📋 Structured Storage**: Saving results in JSONL format for easy analysis
4. **🔄 Continuous Updates**: Daily automated runs ensure fresh data

> **Note**: This is purely for educational and research purposes. No gambling advice is provided.
"""

    @staticmethod
    def get_install_section() -> str:
        """Get installation section."""
        return """## 🚀 Installation & Usage

### 📦 Install via pip

```bash
pip install -i vietlott-data
```

### 💻 Command Line Interface

#### 🔍 Crawl Data

```bash
vietlott-crawl [OPTIONS] PRODUCT

# Options:
#   --run-date TEXT       Specific date to crawl (default: current date)
#   --index-from INTEGER  Starting page index (default: 0)
#   --index-to INTEGER    Ending page index (default: None)
#   --help               Show help message
```

#### 🔧 Backfill Missing Data

```bash
vietlott-missing [OPTIONS] PRODUCT

# Options:
#   --limit INTEGER  Number of pages to process (default: 20)
#   --help          Show help message
```

> **Available Products**: power_655, power_645, power_535, keno, 3d, 3d_pro, bingo18

### 🛠️ Development Setup

```bash
# Clone the repository
git clone https://github.com/haah82/vietlott-data-update.git ; cd vietlott-data-update

# Install dependencies (recommend using uv and virtual environment)
uv sync --dev

# Run tests
uv run pytest
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <strong>⭐ If you find this project useful, please consider giving it a star!</strong>
</div>
"""


def df_to_markdown(df: pl.DataFrame) -> str:
    """Convert Polars DataFrame to Markdown table format."""
    if df.is_empty():
        return "No data available"

    # Get column names
    columns = df.columns

    # Build header
    header = "| " + " | ".join(columns) + " |"
    separator = "| " + " | ".join(["---"] * len(columns)) + " |"

    # Build rows
    rows = []
    for row in df.iter_rows(named=False):
        row_str = "| " + " | ".join(str(val) if val is not None else "" for val in row) + " |"
        rows.append(row_str)

    return "\n".join([header, separator] + rows)


class ReadmeGenerator:
    """Main class for generating the README.md file."""

    def __init__(self):
        self.templates = ReadmeTemplates()

    def _balance_long_df(self, df_: pl.DataFrame, n_splits: int = 20) -> pl.DataFrame:
        """Convert long dataframe to multiple columns for better display."""
        if df_.is_empty():
            return df_

        # Convert all columns to string for display
        df_ = df_.with_columns([pl.col(c).cast(pl.Utf8) for c in df_.columns])

        total_rows = df_.height
        num_chunks = (total_rows // n_splits) + (1 if total_rows % n_splits else 0)

        if num_chunks <= 1:
            return df_

        # Create chunks
        result_frames = []

        for i in range(num_chunks):
            start_idx = i * n_splits
            end_idx = min((i + 1) * n_splits, total_rows)
            chunk = df_.slice(start_idx, end_idx - start_idx)

            if i == 0:
                result_frames.append(chunk)
            else:
                # Add separator column
                separator = pl.DataFrame({f"-{i}": [""] * chunk.height})
                # Rename chunk columns to add prefix
                chunk_renamed = chunk.select([pl.col(c).alias(f"{i}{c}") for c in chunk.columns])
                result_frames.extend([separator, chunk_renamed])

        # Combine horizontally - pad shorter frames with empty strings
        max_height = max(frame.height for frame in result_frames)

        padded_frames = []
        for frame in result_frames:
            if frame.height < max_height:
                # Create padding rows
                padding_rows = max_height - frame.height
                padding_data = {col: [""] * padding_rows for col in frame.columns}
                padding_df = pl.DataFrame(padding_data)
                frame = pl.concat([frame, padding_df])
            padded_frames.append(frame)

        # Concatenate horizontally
        result = pl.concat(padded_frames, how="horizontal")

        return result

    def _load_lottery_data(self, product: str) -> pl.DataFrame:
        """Load and prepare lottery data for analysis."""
        try:
            df = pl.read_ndjson(get_config(product).raw_path)

            # Normalize/parse date column which can be in multiple formats
            if "date" in df.columns:
                # Try to parse the date column
                try:
                    # Check if it's already a date type
                    if df["date"].dtype in [pl.Date, pl.Datetime]:
                        df = df.with_columns(pl.col("date").cast(pl.Date))
                    # Check if it's numeric (epoch time)
                    elif df["date"].dtype in [pl.Int64, pl.Int32, pl.Float64]:
                        # Check if values are in milliseconds or seconds
                        max_val = df["date"].max()
                        if max_val > 1_000_000_000_000:
                            # milliseconds
                            df = df.with_columns(
                                (pl.col("date").cast(pl.Int64) / 1000).cast(pl.Datetime("ms")).cast(pl.Date)
                            )
                        else:
                            # seconds
                            df = df.with_columns(pl.col("date").cast(pl.Int64).cast(pl.Datetime("s")).cast(pl.Date))
                    else:
                        # String date - try to parse
                        df = df.with_columns(pl.col("date").str.to_date(strict=False))
                except Exception as e:
                    logger.warning(f"Could not parse date column: {e}")
                    # Fallback: try string parsing
                    df = df.with_columns(pl.col("date").str.to_date(strict=False))

            df = df.sort(["date", "id"], descending=True)
            return df
        except Exception as e:
            logger.error(f"Error loading data for {product}: {e}")
            return pl.DataFrame()

    def _calculate_stats(self, df: pl.DataFrame) -> pl.DataFrame:
        """Calculate number frequency statistics."""
        if df.is_empty():
            return pl.DataFrame()

        df_explode = df.explode("result")
        stats = df_explode.group_by("result").agg(pl.count("id").alias("count"))
        total_count = df_explode.height
        stats = stats.with_columns(((pl.col("count") / total_count * 100).round(2)).alias("%"))
        stats = stats.sort("count", descending=True)
        return stats

    def _calculate_3d_stats(self, df: pl.DataFrame) -> pl.DataFrame:
        """Calculate number frequency statistics for 3D games where result is a dict."""
        if df.is_empty():
            return pl.DataFrame()

        # Extract all numbers from all prizes
        all_numbers = []
        for row in df.iter_rows(named=True):
            res_dict = row["result"]
            if isinstance(res_dict, dict):
                for prize_nums in res_dict.values():
                    if isinstance(prize_nums, list):
                        all_numbers.extend(prize_nums)
        
        if not all_numbers:
            return pl.DataFrame()
            
        stats_df = pl.Series("result", all_numbers).to_frame().group_by("result").agg(pl.count("result").alias("count"))
        total_count = len(all_numbers)
        stats_df = stats_df.with_columns(((pl.col("count") / total_count * 100).round(2)).alias("%"))
        stats_df = stats_df.sort("count", descending=True)
        return stats_df

    def _get_data_overview(self) -> str:
        """Generate overview statistics for all products."""
        products = ["power_655", "power_645", "power_535", "keno", "3d", "3d_pro", "bingo18"]
        data_stats = []

        for product in products:
            try:
                df = self._load_lottery_data(product)
                if not df.is_empty():
                    data_stats.append(
                        {
                            "Product": product.replace("_", " ").title(),
                            "Total Draws": df["date"].n_unique(),
                            "Start Date": str(df["date"].min()),
                            "End Date": str(df["date"].max()),
                            "Total Records": df["id"].n_unique(),
                            "First ID": str(df["id"].min()),
                            "Latest ID": str(df["id"].max()),
                        }
                    )
            except Exception as e:
                logger.warning(f"Could not load stats for {product}: {e}")

        if data_stats:
            df_stats = pl.DataFrame(data_stats)
            return df_to_markdown(df_stats)
        return "No data available"

    def _generate_power_analysis(self, df: pl.DataFrame, title: str, stats_all_orig: pl.DataFrame = None) -> str:
        """Generate detailed Power analysis section."""
        if df.is_empty():
            return f"## {title}\n\n> No data available for analysis.\n"

        try:
            # Calculate stats for different periods
            if stats_all_orig is None:
                stats_all_orig = self._calculate_stats(df)
            
            stats_all = self._balance_long_df(stats_all_orig)

            current_date = datetime.now().date()
            stats_30d = self._balance_long_df(
                self._calculate_stats(df.filter(pl.col("date") >= (current_date - timedelta(days=30))))
            )
            stats_60d = self._balance_long_df(
                self._calculate_stats(df.filter(pl.col("date") >= (current_date - timedelta(days=60))))
            )
            stats_90d = self._balance_long_df(
                self._calculate_stats(df.filter(pl.col("date") >= (current_date - timedelta(days=90))))
            )

            recent_results = df.head(10)

            # Convert to markdown
            recent_results_md = df_to_markdown(recent_results)
            stats_all_md = df_to_markdown(stats_all)
            stats_30d_md = df_to_markdown(stats_30d)
            stats_60d_md = df_to_markdown(stats_60d)
            stats_90d_md = df_to_markdown(stats_90d)

            return f"""## {title}

### 📅 Recent Results (Last 10 draws)
{recent_results_md}

### 🎲 Number Frequency (All Time)
{stats_all_md}

### 📊 Frequency Analysis by Period

#### Last 30 Days
{stats_30d_md}

#### Last 60 Days
{stats_60d_md}

#### Last 90 Days
{stats_90d_md}
"""
        except Exception as e:
            logger.exception(f"Error generating {title}: {e}")
            return f"## {title}\n\n> Error generating analysis.\n"

    def _generate_3d_analysis(self, df: pl.DataFrame, title: str) -> str:
        """Generate detailed 3D analysis section."""
        if df.is_empty():
            return f"## {title}\n\n> No data available for analysis.\n"

        try:
            stats_all = self._balance_long_df(self._calculate_3d_stats(df).head(100)) # Show top 100 for 3D
            recent_results = df.head(10)
            
            # For 3D we need to format the result dict for display
            recent_results_formatted = recent_results.with_columns(
                pl.col("result").map_elements(lambda d: ", ".join(itertools.chain.from_iterable(d.values())), return_dtype=pl.Utf8)
            )

            recent_md = df_to_markdown(recent_results_formatted)
            stats_md = df_to_markdown(stats_all)

            return f"""## {title}

### 📅 Recent Results (Last 10 draws)
{recent_md}

### 🎲 Top 3-Digit Number Frequency (All Time)
{stats_md}
"""
        except Exception as e:
            logger.exception(f"Error generating {title}: {e}")
            return f"## {title}\n\n> Error generating analysis.\n"

    def _generate_top_probability_summary(self, product_stats: dict) -> str:
        """Generate a summary of top 10 highest probability numbers across products."""
        summary_rows = []
        
        for name, stats in product_stats.items():
            if stats.is_empty():
                continue
            
            top_10 = stats.head(10).to_dicts()
            for i, row in enumerate(top_10):
                summary_rows.append({
                    "Rank": i + 1,
                    "Product": name,
                    "Number/Set": row["result"],
                    "Probability (%)": row["%"]
                })
        
        if not summary_rows:
            return ""
            
        df_summary = pl.DataFrame(summary_rows).sort(["Rank", "Product"])
        md = df_to_markdown(df_summary)
        
        return f"""## 🏆 Top Probability Summary

This table shows the top 10 most frequent results (highest weights) for each major product.

{md}
"""

    def _generate_pair_matrix_plot(self, df: pl.DataFrame, product_name: str = "Power 6/55") -> str:
        """Generate a heatmap of number pairs and save it as an image."""
        try:
            if df.is_empty():
                return ""

            # Extract results and find pairs
            results = df["result"].to_list()
            # Convert string representations of lists to actual lists if necessary
            # (Though in our repo they should already be lists from read_ndjson)
            
            pair_counts = Counter()
            for draw in results:
                if isinstance(draw, list) and len(draw) >= 2:
                    # Sort to ensure (1, 2) is same as (2, 1)
                    sorted_draw = sorted([int(x) for x in draw[:6]]) # Focus on first 6 numbers
                    pairs = itertools.combinations(sorted_draw, 2)
                    pair_counts.update(pairs)

            if not pair_counts:
                return ""

            # Create matrix
            max_num = 55 # For Power 6/55
            matrix = np.zeros((max_num + 1, max_num + 1))
            for (n1, n2), count in pair_counts.items():
                matrix[n1][n2] = count
                matrix[n2][n1] = count

            # Plotting
            plt.figure(figsize=(12, 10))
            plt.imshow(matrix[1:, 1:], cmap='YlOrRd', interpolation='nearest')
            plt.colorbar(label='Frequency')
            plt.title(f'Number Pairs Frequency Matrix - {product_name}')
            plt.xlabel('Number')
            plt.ylabel('Number')
            
            # Save to assets
            output_dir = Path(__file__).parent.parent / "assets" / "images"
            output_dir.mkdir(parents=True, exist_ok=True)
            output_path = output_dir / "pairs_matrix.png"
            plt.savefig(output_path, bbox_inches='tight', dpi=150)
            plt.close()
            
            logger.info(f"Generated pair matrix plot at {output_path}")
            return f"\n### 📊 Visualized Analysis\n\n![Number Pairs Frequency Matrix](./assets/images/pairs_matrix.png)\n"
        except Exception as e:
            logger.error(f"Error generating pair matrix plot: {e}")
            return ""

    def generate_readme(self) -> str:
        """Generate the complete README content."""
        logger.info("Starting README generation...")

        # Load data
        df_power655 = self._load_lottery_data("power_655")
        df_power645 = self._load_lottery_data("power_645")
        df_3d = self._load_lottery_data("3d")
        df_3d_pro = self._load_lottery_data("3d_pro")

        # Pre-calculate stats for summary
        stats_data = {
            "Power 6/55": self._calculate_stats(df_power655),
            "Power 6/45": self._calculate_stats(df_power645),
            "Max 3D Plus": self._calculate_3d_stats(df_3d),
            "Max 3D Pro": self._calculate_3d_stats(df_3d_pro),
        }

        # Generate all sections
        header = self.templates.get_header()
        toc = self.templates.get_toc()
        data_overview = self._get_data_overview()
        
        # Summary table
        probability_summary = self._generate_top_probability_summary(stats_data)
        
        # New visualization
        visualization = self._generate_pair_matrix_plot(df_power655)
        
        power655_analysis = self._generate_power_analysis(df_power655, "📈 Power 6/55 Analysis", stats_data["Power 6/55"])
        power645_analysis = self._generate_power_analysis(df_power645, "📈 Power 6/45 Analysis", stats_data["Power 6/45"])
        
        max3d_plus_analysis = self._generate_3d_analysis(df_3d, "📈 Max 3D Plus Analysis")
        max3d_pro_analysis = self._generate_3d_analysis(df_3d_pro, "📈 Max 3D Pro Analysis")
        
        how_it_works = self.templates.get_how_it_works()
        install_section = self.templates.get_install_section()

        # Combine all sections
        readme_content = f"""{header}

{toc}

{probability_summary}

## Predictions

Models and predictions are updated daily at [/src/predictions](./src/machine_learning/prediction_summary.md)

## 📊 Data Statistics

{data_overview}

{visualization}

{power655_analysis}

{power645_analysis}

{max3d_plus_analysis}

{max3d_pro_analysis}

{how_it_works}

{install_section}
"""

        return readme_content

    def save_readme(self, output_path: Optional[Path] = None) -> None:
        """Generate and save README to file."""
        if output_path is None:
            output_path = Path("./readme.md")

        try:
            readme_content = self.generate_readme()

            with output_path.open("w", encoding="utf-8") as ofile:
                ofile.write(readme_content)

            logger.info(f"README successfully written to {output_path.absolute()}")
        except Exception as e:
            logger.error(f"Error saving README: {e}")
            raise


def main():
    """Main entry point for README generation."""
    try:
        generator = ReadmeGenerator()
        generator.save_readme()
        logger.info("README generation completed successfully!")
    except Exception as e:
        logger.error(f"Failed to generate README: {e}")
        # Not raising here to prevent workflow failure if just README fails
        import sys
        sys.exit(0) 

if __name__ == "__main__":
    main()
