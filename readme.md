# 🎰 Vietlott Data

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


## 📋 Table of Contents

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
- [⚙️ How It Works](#️-how-it-works)
- [🚀 Installation & Usage](#-installation--usage)
- [📄 License](#-license)


## Predictions

Predicitons models are at [/src/predictions](./src/machine_learning/prediction_summary.md)

## 📊 Data Statistics

| Product | Total Draws | Start Date | End Date | Total Records | First ID | Latest ID |
| --- | --- | --- | --- | --- | --- | --- |
| Power 655 | 1292 | 2017-08-01 | 2026-01-08 | 1292 | 00001 | 01292 |
| Power 645 | 1259 | 2017-10-25 | 2026-01-09 | 1259 | 00198 | 01456 |
| Power 535 | 161 | 2025-06-29 | 2026-01-09 | 320 | 00001 | 00389 |
| Keno | 411 | 2022-12-04 | 2026-01-09 | 52875 | #0110271 | #0266204 |
| 3D | 1023 | 2019-04-22 | 2026-01-09 | 1023 | 00001 | 01027 |
| 3D Pro | 669 | 2021-09-14 | 2026-01-08 | 669 | 00001 | 00673 |
| Bingo18 | 386 | 2024-12-03 | 2026-01-09 | 52836 | 0083123 | 0147068 |


### 📊 Visualized Analysis

![Number Pairs Frequency Matrix](./assets/images/pairs_matrix.png)


## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-01-08 | 01292 | [20, 22, 36, 43, 45, 50, 47] | 2026-01-09T18:53:58.591551 |
| 2026-01-06 | 01291 | [22, 28, 29, 30, 34, 47, 20] | 2026-01-09T18:53:58.591650 |
| 2026-01-03 | 01290 | [10, 16, 17, 23, 33, 36, 42] | 2026-01-09T18:53:58.591714 |
| 2026-01-01 | 01289 | [5, 16, 29, 33, 39, 42, 54] | 2026-01-09T18:53:58.591773 |
| 2025-12-30 | 01288 | [11, 30, 35, 41, 48, 55, 38] | 2026-01-09T18:53:58.591828 |
| 2025-12-27 | 01287 | [16, 21, 30, 37, 39, 40, 13] | 2026-01-09T18:53:58.591883 |
| 2025-12-25 | 01286 | [4, 6, 32, 37, 40, 48, 38] | 2026-01-09T18:53:58.591934 |
| 2025-12-23 | 01285 | [2, 10, 16, 25, 32, 38, 3] | 2026-01-09T18:53:58.591986 |
| 2025-12-20 | 01284 | [22, 32, 33, 35, 40, 41, 23] | 2025-12-21T00:00:50.783917 |
| 2025-12-18 | 01283 | [12, 14, 29, 30, 39, 55, 50] | 2025-12-19T00:00:54.542458 |

### 🎲 Number Frequency (All Time)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 41 | 192 | 2.12 |  | 32 | 169 | 1.87 |  | 39 | 156 | 1.73 |
| 22 | 188 | 2.08 |  | 46 | 168 | 1.86 |  | 10 | 156 | 1.73 |
| 43 | 186 | 2.06 |  | 52 | 168 | 1.86 |  | 54 | 154 | 1.7 |
| 51 | 184 | 2.03 |  | 24 | 167 | 1.85 |  | 15 | 153 | 1.69 |
| 34 | 184 | 2.03 |  | 33 | 167 | 1.85 |  | 27 | 152 | 1.68 |
| 40 | 181 | 2.0 |  | 18 | 166 | 1.84 |  | 37 | 150 | 1.66 |
| 9 | 180 | 1.99 |  | 19 | 166 | 1.84 |  | 26 | 150 | 1.66 |
| 20 | 177 | 1.96 |  | 5 | 166 | 1.84 |  | 30 | 149 | 1.65 |
| 8 | 177 | 1.96 |  | 45 | 165 | 1.82 |  | 17 | 149 | 1.65 |
| 48 | 176 | 1.95 |  | 14 | 165 | 1.82 |  | 2 | 149 | 1.65 |
| 23 | 176 | 1.95 |  | 47 | 165 | 1.82 |  | 25 | 144 | 1.59 |
| 3 | 175 | 1.94 |  | 49 | 164 | 1.81 |  | 28 | 144 | 1.59 |
| 29 | 175 | 1.94 |  | 50 | 164 | 1.81 |  | 7 | 141 | 1.56 |
| 1 | 173 | 1.91 |  | 55 | 163 | 1.8 |  | 6 | 139 | 1.54 |
| 31 | 173 | 1.91 |  | 35 | 162 | 1.79 |  | 4 | 136 | 1.5 |
| 12 | 172 | 1.9 |  | 38 | 159 | 1.76 |  |  |  |  |
| 42 | 170 | 1.88 |  | 21 | 158 | 1.75 |  |  |  |  |
| 11 | 170 | 1.88 |  | 16 | 157 | 1.74 |  |  |  |  |
| 53 | 170 | 1.88 |  | 13 | 157 | 1.74 |  |  |  |  |
| 44 | 170 | 1.88 |  | 36 | 156 | 1.73 |  |  |  |  |

### 📊 Frequency Analysis by Period

#### Last 30 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 38 | 6 | 6.59 |  | 5 | 2 | 2.2 |  | 25 | 1 | 1.1 |
| 30 | 4 | 4.4 |  | 50 | 2 | 2.2 |  | 6 | 1 | 1.1 |
| 55 | 4 | 4.4 |  | 42 | 2 | 2.2 |  | 2 | 1 | 1.1 |
| 16 | 4 | 4.4 |  | 23 | 2 | 2.2 |  | 14 | 1 | 1.1 |
| 20 | 3 | 3.3 |  | 10 | 2 | 2.2 |  |  |  |  |
| 48 | 3 | 3.3 |  | 52 | 2 | 2.2 |  |  |  |  |
| 39 | 3 | 3.3 |  | 41 | 2 | 2.2 |  |  |  |  |
| 22 | 3 | 3.3 |  | 11 | 1 | 1.1 |  |  |  |  |
| 40 | 3 | 3.3 |  | 7 | 1 | 1.1 |  |  |  |  |
| 37 | 3 | 3.3 |  | 9 | 1 | 1.1 |  |  |  |  |
| 33 | 3 | 3.3 |  | 8 | 1 | 1.1 |  |  |  |  |
| 32 | 3 | 3.3 |  | 18 | 1 | 1.1 |  |  |  |  |
| 29 | 3 | 3.3 |  | 46 | 1 | 1.1 |  |  |  |  |
| 36 | 3 | 3.3 |  | 4 | 1 | 1.1 |  |  |  |  |
| 12 | 2 | 2.2 |  | 54 | 1 | 1.1 |  |  |  |  |
| 13 | 2 | 2.2 |  | 17 | 1 | 1.1 |  |  |  |  |
| 47 | 2 | 2.2 |  | 43 | 1 | 1.1 |  |  |  |  |
| 45 | 2 | 2.2 |  | 28 | 1 | 1.1 |  |  |  |  |
| 35 | 2 | 2.2 |  | 3 | 1 | 1.1 |  |  |  |  |
| 21 | 2 | 2.2 |  | 34 | 1 | 1.1 |  |  |  |  |

#### Last 60 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 38 | 8 | 4.4 |  | 4 | 4 | 2.2 |  | 3 | 2 | 1.1 |
| 20 | 7 | 3.85 |  | 35 | 4 | 2.2 |  | 9 | 2 | 1.1 |
| 30 | 7 | 3.85 |  | 22 | 4 | 2.2 |  | 18 | 2 | 1.1 |
| 10 | 6 | 3.3 |  | 43 | 3 | 1.65 |  | 19 | 2 | 1.1 |
| 42 | 6 | 3.3 |  | 52 | 3 | 1.65 |  | 24 | 2 | 1.1 |
| 29 | 5 | 2.75 |  | 23 | 3 | 1.65 |  | 27 | 2 | 1.1 |
| 48 | 5 | 2.75 |  | 50 | 3 | 1.65 |  | 2 | 2 | 1.1 |
| 40 | 5 | 2.75 |  | 41 | 3 | 1.65 |  | 25 | 1 | 0.55 |
| 12 | 5 | 2.75 |  | 21 | 3 | 1.65 |  | 17 | 1 | 0.55 |
| 32 | 5 | 2.75 |  | 28 | 3 | 1.65 |  | 53 | 1 | 0.55 |
| 33 | 5 | 2.75 |  | 39 | 3 | 1.65 |  | 6 | 1 | 0.55 |
| 16 | 5 | 2.75 |  | 45 | 3 | 1.65 |  | 44 | 1 | 0.55 |
| 31 | 4 | 2.2 |  | 46 | 3 | 1.65 |  | 51 | 1 | 0.55 |
| 5 | 4 | 2.2 |  | 11 | 3 | 1.65 |  | 1 | 1 | 0.55 |
| 36 | 4 | 2.2 |  | 47 | 3 | 1.65 |  | 49 | 1 | 0.55 |
| 14 | 4 | 2.2 |  | 34 | 3 | 1.65 |  |  |  |  |
| 54 | 4 | 2.2 |  | 15 | 2 | 1.1 |  |  |  |  |
| 55 | 4 | 2.2 |  | 7 | 2 | 1.1 |  |  |  |  |
| 13 | 4 | 2.2 |  | 26 | 2 | 1.1 |  |  |  |  |
| 37 | 4 | 2.2 |  | 8 | 2 | 1.1 |  |  |  |  |

#### Last 90 Days
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 38 | 10 | 3.76 |  | 37 | 6 | 2.26 |  | 18 | 3 | 1.13 |
| 16 | 9 | 3.38 |  | 21 | 5 | 1.88 |  | 34 | 3 | 1.13 |
| 20 | 9 | 3.38 |  | 54 | 5 | 1.88 |  | 39 | 3 | 1.13 |
| 10 | 8 | 3.01 |  | 45 | 5 | 1.88 |  | 46 | 3 | 1.13 |
| 29 | 8 | 3.01 |  | 50 | 5 | 1.88 |  | 49 | 3 | 1.13 |
| 33 | 7 | 2.63 |  | 13 | 5 | 1.88 |  | 52 | 3 | 1.13 |
| 22 | 7 | 2.63 |  | 43 | 5 | 1.88 |  | 7 | 3 | 1.13 |
| 40 | 7 | 2.63 |  | 32 | 5 | 1.88 |  | 6 | 3 | 1.13 |
| 36 | 7 | 2.63 |  | 41 | 5 | 1.88 |  | 2 | 2 | 0.75 |
| 30 | 7 | 2.63 |  | 35 | 5 | 1.88 |  | 44 | 2 | 0.75 |
| 12 | 7 | 2.63 |  | 4 | 4 | 1.5 |  | 25 | 2 | 0.75 |
| 14 | 7 | 2.63 |  | 3 | 4 | 1.5 |  | 51 | 1 | 0.38 |
| 11 | 6 | 2.26 |  | 47 | 4 | 1.5 |  | 17 | 1 | 0.38 |
| 5 | 6 | 2.26 |  | 19 | 4 | 1.5 |  | 53 | 1 | 0.38 |
| 55 | 6 | 2.26 |  | 26 | 4 | 1.5 |  | 1 | 1 | 0.38 |
| 42 | 6 | 2.26 |  | 15 | 4 | 1.5 |  |  |  |  |
| 27 | 6 | 2.26 |  | 23 | 4 | 1.5 |  |  |  |  |
| 48 | 6 | 2.26 |  | 9 | 4 | 1.5 |  |  |  |  |
| 8 | 6 | 2.26 |  | 28 | 4 | 1.5 |  |  |  |  |
| 31 | 6 | 2.26 |  | 24 | 4 | 1.5 |  |  |  |  |



## 📈 Power 6/45 Analysis

### 📅 Recent Results (Last 10 draws) (6/45)
| date | id | result | process_time |
| --- | --- | --- | --- |
| 2026-01-09 | 01456 | [8, 9, 17, 21, 36, 45] | 2026-01-09T18:55:03.608163 |
| 2026-01-07 | 01455 | [1, 5, 7, 28, 31, 43] | 2026-01-09T18:55:03.608263 |
| 2026-01-04 | 01454 | [2, 12, 21, 29, 35, 44] | 2026-01-09T18:55:03.608339 |
| 2026-01-02 | 01453 | [7, 18, 22, 32, 37, 38] | 2026-01-09T18:55:03.608413 |
| 2025-12-31 | 01452 | [1, 25, 35, 36, 37, 45] | 2026-01-09T18:55:03.608480 |
| 2025-12-28 | 01451 | [1, 2, 7, 16, 31, 37] | 2026-01-09T18:55:03.608545 |
| 2025-12-26 | 01450 | [4, 6, 16, 25, 27, 40] | 2026-01-09T18:55:03.608607 |
| 2025-12-24 | 01449 | [15, 19, 31, 35, 43, 45] | 2026-01-09T18:55:03.608666 |
| 2025-12-21 | 01448 | [6, 9, 12, 18, 29, 43] | 2025-12-22T00:01:15.347990 |
| 2025-12-19 | 01447 | [1, 21, 36, 42, 43, 44] | 2025-12-20T00:01:12.378702 |

### 🎲 Number Frequency (All Time) (6/45)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 24 | 187 | 2.48 |  | 13 | 168 | 2.22 |  | 2 | 154 | 2.04 |
| 10 | 187 | 2.48 |  | 1 | 168 | 2.22 |  | 12 | 152 | 2.01 |
| 19 | 187 | 2.48 |  | 31 | 168 | 2.22 |  | 32 | 152 | 2.01 |
| 7 | 185 | 2.45 |  | 26 | 168 | 2.22 |  | 38 | 146 | 1.93 |
| 28 | 183 | 2.42 |  | 43 | 167 | 2.21 |  | 17 | 145 | 1.92 |
| 37 | 182 | 2.41 |  | 25 | 167 | 2.21 |  |  |  |  |
| 22 | 182 | 2.41 |  | 23 | 167 | 2.21 |  |  |  |  |
| 44 | 181 | 2.4 |  | 6 | 165 | 2.18 |  |  |  |  |
| 30 | 178 | 2.36 |  | 16 | 165 | 2.18 |  |  |  |  |
| 20 | 177 | 2.34 |  | 8 | 165 | 2.18 |  |  |  |  |
| 4 | 176 | 2.33 |  | 42 | 164 | 2.17 |  |  |  |  |
| 41 | 175 | 2.32 |  | 33 | 164 | 2.17 |  |  |  |  |
| 34 | 174 | 2.3 |  | 14 | 163 | 2.16 |  |  |  |  |
| 29 | 174 | 2.3 |  | 9 | 159 | 2.1 |  |  |  |  |
| 27 | 173 | 2.29 |  | 39 | 158 | 2.09 |  |  |  |  |
| 11 | 172 | 2.28 |  | 36 | 157 | 2.08 |  |  |  |  |
| 18 | 171 | 2.26 |  | 40 | 157 | 2.08 |  |  |  |  |
| 35 | 170 | 2.25 |  | 3 | 155 | 2.05 |  |  |  |  |
| 45 | 169 | 2.24 |  | 15 | 154 | 2.04 |  |  |  |  |
| 5 | 169 | 2.24 |  | 21 | 154 | 2.04 |  |  |  |  |

### 📊 Frequency Analysis by Period (6/45)

#### Last 30 Days (6/45)
| result | count | % | -1 | 1result | 1count | 1% |
| --- | --- | --- | --- | --- | --- | --- |
| 43 | 5 | 6.41 |  | 17 | 2 | 2.56 |
| 1 | 4 | 5.13 |  | 9 | 2 | 2.56 |
| 7 | 4 | 5.13 |  | 8 | 2 | 2.56 |
| 31 | 3 | 3.85 |  | 12 | 2 | 2.56 |
| 44 | 3 | 3.85 |  | 18 | 2 | 2.56 |
| 38 | 3 | 3.85 |  | 24 | 1 | 1.28 |
| 35 | 3 | 3.85 |  | 4 | 1 | 1.28 |
| 45 | 3 | 3.85 |  | 27 | 1 | 1.28 |
| 21 | 3 | 3.85 |  | 42 | 1 | 1.28 |
| 37 | 3 | 3.85 |  | 22 | 1 | 1.28 |
| 16 | 3 | 3.85 |  | 19 | 1 | 1.28 |
| 36 | 3 | 3.85 |  | 11 | 1 | 1.28 |
| 29 | 2 | 2.56 |  | 41 | 1 | 1.28 |
| 13 | 2 | 2.56 |  | 15 | 1 | 1.28 |
| 2 | 2 | 2.56 |  | 40 | 1 | 1.28 |
| 32 | 2 | 2.56 |  | 14 | 1 | 1.28 |
| 25 | 2 | 2.56 |  | 3 | 1 | 1.28 |
| 6 | 2 | 2.56 |  |  |  |  |
| 5 | 2 | 2.56 |  |  |  |  |
| 28 | 2 | 2.56 |  |  |  |  |

#### Last 60 Days (6/45)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 43 | 9 | 5.77 |  | 12 | 4 | 2.56 |  | 26 | 1 | 0.64 |
| 7 | 6 | 3.85 |  | 30 | 4 | 2.56 |  | 14 | 1 | 0.64 |
| 42 | 5 | 3.21 |  | 45 | 4 | 2.56 |  | 10 | 1 | 0.64 |
| 2 | 5 | 3.21 |  | 25 | 3 | 1.92 |  | 33 | 1 | 0.64 |
| 29 | 5 | 3.21 |  | 21 | 3 | 1.92 |  | 39 | 1 | 0.64 |
| 37 | 5 | 3.21 |  | 13 | 3 | 1.92 |  |  |  |  |
| 8 | 5 | 3.21 |  | 5 | 3 | 1.92 |  |  |  |  |
| 1 | 5 | 3.21 |  | 41 | 3 | 1.92 |  |  |  |  |
| 44 | 5 | 3.21 |  | 17 | 3 | 1.92 |  |  |  |  |
| 19 | 5 | 3.21 |  | 34 | 3 | 1.92 |  |  |  |  |
| 31 | 5 | 3.21 |  | 40 | 3 | 1.92 |  |  |  |  |
| 15 | 5 | 3.21 |  | 20 | 2 | 1.28 |  |  |  |  |
| 38 | 4 | 2.56 |  | 32 | 2 | 1.28 |  |  |  |  |
| 18 | 4 | 2.56 |  | 3 | 2 | 1.28 |  |  |  |  |
| 35 | 4 | 2.56 |  | 27 | 2 | 1.28 |  |  |  |  |
| 28 | 4 | 2.56 |  | 11 | 2 | 1.28 |  |  |  |  |
| 16 | 4 | 2.56 |  | 4 | 2 | 1.28 |  |  |  |  |
| 36 | 4 | 2.56 |  | 6 | 2 | 1.28 |  |  |  |  |
| 9 | 4 | 2.56 |  | 22 | 2 | 1.28 |  |  |  |  |
| 23 | 4 | 2.56 |  | 24 | 2 | 1.28 |  |  |  |  |

#### Last 90 Days (6/45)
| result | count | % | -1 | 1result | 1count | 1% | -2 | 2result | 2count | 2% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 43 | 12 | 5.13 |  | 23 | 5 | 2.14 |  | 27 | 3 | 1.28 |
| 31 | 9 | 3.85 |  | 36 | 5 | 2.14 |  | 21 | 3 | 1.28 |
| 42 | 9 | 3.85 |  | 8 | 5 | 2.14 |  | 22 | 2 | 0.85 |
| 30 | 8 | 3.42 |  | 38 | 5 | 2.14 |  | 33 | 1 | 0.43 |
| 7 | 8 | 3.42 |  | 9 | 5 | 2.14 |  | 14 | 1 | 0.43 |
| 28 | 8 | 3.42 |  | 35 | 5 | 2.14 |  |  |  |  |
| 18 | 8 | 3.42 |  | 19 | 5 | 2.14 |  |  |  |  |
| 44 | 7 | 2.99 |  | 45 | 5 | 2.14 |  |  |  |  |
| 37 | 7 | 2.99 |  | 40 | 4 | 1.71 |  |  |  |  |
| 2 | 7 | 2.99 |  | 41 | 4 | 1.71 |  |  |  |  |
| 29 | 6 | 2.56 |  | 4 | 4 | 1.71 |  |  |  |  |
| 16 | 6 | 2.56 |  | 11 | 4 | 1.71 |  |  |  |  |
| 12 | 6 | 2.56 |  | 24 | 4 | 1.71 |  |  |  |  |
| 20 | 6 | 2.56 |  | 13 | 4 | 1.71 |  |  |  |  |
| 34 | 6 | 2.56 |  | 5 | 4 | 1.71 |  |  |  |  |
| 15 | 6 | 2.56 |  | 26 | 4 | 1.71 |  |  |  |  |
| 1 | 6 | 2.56 |  | 6 | 3 | 1.28 |  |  |  |  |
| 25 | 5 | 2.14 |  | 32 | 3 | 1.28 |  |  |  |  |
| 3 | 5 | 2.14 |  | 10 | 3 | 1.28 |  |  |  |  |
| 17 | 5 | 2.14 |  | 39 | 3 | 1.28 |  |  |  |  |



## ⚙️ How It Works

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


## 🚀 Installation & Usage

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

