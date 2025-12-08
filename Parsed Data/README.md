# Parsed Data

This folder contains **143 parsed CSV files**, each representing one subject's 10-minute navigation session in the VR learning maze.

## Data Format

| Column | Description |
|--------|-------------|
| `date/time` | Timestamp of the recording |
| `seconds since started` | Time in seconds from session start |
| `posX` | X position in the maze |
| `posY` | Y position (height) |
| `posZ` | Z position in the maze |
| `rotX` | Head rotation X (pitch) |
| `rotY` | Head rotation Y (yaw) |
| `rotZ` | Head rotation Z (roll) |

## Data Characteristics

- **Sampling rate:** ~50 Hz (20ms intervals)
- **Duration:** ~10 minutes per subject
- **Rows per file:** ~30,000 data points
- **Total subjects:** 143

## Example

```csv
date/time,seconds since started,posX,posY,posZ,rotX,rotY,rotZ
12/03/2018 13:28:25,309.94,1.270441,1.743523,-4.205029,8.775977,265.6833,355.2423
12/03/2018 13:29:50,394.6,0.0,0.0,-1.658,9.898545,91.13422,358.847
...
```

## Usage

```python
import pandas as pd

df = pd.read_csv('Parsed Data/AAAA.csv')
print(df.shape)  # (30000, 8)
```

---

# Appendix: Subject Processing Status

The following table documents how each subject's data was processed from the raw experimental files.

## Status Codes

| Code | Meaning |
|------|---------|
| **Y** / **V** | Data parsed perfectly by the algorithm |
| **N** | Required hardcoded 10-minute shift (algorithm found training maze instead of learning maze) |
| **X** | Data discarded (visual made no sense even after manual adjustment) |

---

## Labeled Data

| Subject ID | Status | Notes |
|------------|--------|-------|
| IZZO | X | |
| SVBB | X | |
| RCEH | N | |
| VUUK | X | |
| IXRA | N | |
| FMVE Bad | X | |
| CXIJ | N | |
| DKAF | X | |
| RTUG | V | |
| CPSL | V | |
| JHMW | X | |
| NWTC | X | |
| YBRX | X | |
| MLOS | X | |
| KMRY | X | |
| CDYY | X | |
| LQKJ | V | |
| AOXY | N | |
| WGNY | V | |
| UVRZ | N | |
| OGTB | N | |
| BPPX | N | |
| GJJJ | N | |
| YFDE | N | |
| RIKR | N | |
| YJKM | N | |
| XLLZ | X | |
| UNWN | X | |
| VPQA | N | |
| MPOB | N | |
| UPCV | X | |
| OUWM | N | |
| JBXP | N | |
| VZYX | N | |
| RSXQ | X | |
| YPQL | N | |
| WMKQ | N | |
| HASK | N | |
| UFNF | N | |
| IHGX | N | |
| TMPJ | N | |
| ZTAL | N | |
| VNWM | N | |
| ODJH | N | |
| SIUT | N | |
| XLZQ | X | |
| DRDQ | N | |
| FXXV | N | |
| EGRU | N | |
| ZDGH | N | |
| TEYQ | N | |
| VKPD | N | |
| TYJR | N | |
| YNRZ | N | |
| RGYJ | N | |
| ANAV | N | |
| URXR | N | |
| NGVO | N | |
| QQTV | N | |
| RTBV | N | |
| OWHE | N | |
| QVFJ | N | |
| CGWN | N | |
| LAWW | N | |
| BVEH | N | |
| DXJP | N | |
| PGBB | N | |
| MRPD | N | |
| JVRV | N | |
| MTXB | N | |
| KSQU | N | 2 candidates |
| NUAO | N | |
| FWPA | V | 2 candidates |
| CXQX | N | |
| EOPT | N | |
| OGBK | N | |
| WTIY | N | |
| GZTO | N | |
| EUDK | N | |
| GQYU | X | 2 candidates |
| UPGW | N | |
| SSNK | N | 2 candidates |
| IQMQ | N | |
| GGWU | N | |
| DBQH | N | |
| ZDNA | X | |
| YYTZ | N | 2 candidates |
| XQJO | N | |
| UICN | N | |
| HRGF | N | |
| ONVA | N | |
| TWJS | X | 2 candidates |
| WONG | N | |
| MCCO | N | |

---

## Unlabeled Data

| Subject ID | Status | Notes |
|------------|--------|-------|
| AAAA | N | |
| ACGN | N | |
| AELV | N | |
| BBBB | X | |
| BBHD | V | |
| BFFT | V | |
| BFJK | N | |
| BPUF | V | |
| BQHT | N | |
| BWNF | V | |
| BYOU | N | |
| CBDG | N | |
| CFLN | X | |
| CXYL | V | |
| DIJR | V | |
| EMBJ | N | |
| FAFH | V | |
| FGTV | N | 2 candidates |
| FIVC | N | |
| FJAJ | X | |
| FJEB | V | |
| FMKJ | N | |
| FMRE | N | |
| FPIT | N | |
| FQGS | N | |
| FQMM | V | |
| FVZI | V | |
| FWVY | V | |
| GCIV | V | |
| GGMO | N | |
| HCWV | V | |
| HDNQ | V | |
| HIXM | V | |
| HTLW | N | |
| IAHA | X | |
| IIMV | V | |
| ITCT | V | |
| JKOY | V | |
| JYVB | V | |
| KRKM | N | |
| KXKS | N | |
| LCPU | V | |
| LFWZ | N | |
| LMUU | V | |
| LVEY | V | |
| MEPW | X | |
| MHGM | V | |
| NEQV | X | |
| OVOW | N | |
| PGJC | N | |
| QHTL | N | |
| QKVF | X | |
| QMGI | N | |
| QMUX | V | |
| QZPJ | V | |
| RRSK | V | |
| RVQO | N | |
| SFUG | N | |
| SGLD | N | |
| SSXP | V | |
| test | — | Test file |
| TRTT | V | |
| TRUK | V | |
| TWBG | V | |
| UING | N | |
| UREH | N | |
| UZMT | N | |
| VAGY | V | |
| VCVG | V | |
| VJGB | V | |
| WFKT | V | |
| WJJU | N | |
| WOKD | N | |
| WRED | V | |
| WTYX | X | |
| XBCP | V | |
| XKAL | N | |
| XPRU | N | |
| YDJH | X | |
| YLTR | V | |
| YPGZ | N | |

