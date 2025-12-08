# 📊 Parsed Data

This folder contains **143 parsed CSV files**, each representing one subject's 10-minute navigation session in the VR learning maze.

---

## 📁 Data Format

| Column | Type | Description |
|--------|------|-------------|
| `date/time` | datetime | Timestamp of the recording |
| `seconds since started` | float | Time in seconds from session start |
| `posX` | float | X position in the maze |
| `posY` | float | Y position (height) |
| `posZ` | float | Z position in the maze |
| `rotX` | float | Head rotation X (pitch) |
| `rotY` | float | Head rotation Y (yaw) |
| `rotZ` | float | Head rotation Z (roll) |

---

## 📈 Data Characteristics

| Property | Value |
|----------|-------|
| **Sampling Rate** | ~50 Hz (20ms intervals) |
| **Duration** | ~10 minutes per subject |
| **Rows per File** | ~30,000 data points |
| **Total Subjects** | 143 |
| **File Format** | CSV (comma-separated) |

---

## 💻 Usage Example

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load a subject's data
df = pd.read_csv('Parsed Data/AAAA.csv')

print(f"Shape: {df.shape}")          # (30000, 8)
print(f"Duration: {df['seconds since started'].max():.0f}s")

# Quick visualization
plt.scatter(df['posX'], df['posZ'], s=1, alpha=0.5)
plt.xlabel('X Position')
plt.ylabel('Z Position')
plt.title('Subject Navigation Path')
plt.show()
```

---

## 📄 Sample Data

```csv
date/time,seconds since started,posX,posY,posZ,rotX,rotY,rotZ
12/03/2018 13:28:25,309.94,1.270441,1.743523,-4.205029,8.775977,265.6833,355.2423
12/03/2018 13:29:50,394.60,0.000000,0.000000,-1.658000,9.898545,91.13422,358.8470
...
```

---

## 🗂️ File List

<details>
<summary>Click to expand all 143 subject files</summary>

```
AAAA.csv   ACGN.csv   AELV.csv   ANAV.csv   AOXY.csv   BBHD.csv   
BFFT.csv   BFJK.csv   BPPX.csv   BPUF.csv   BQHT.csv   BVEH.csv   
BWNF.csv   BYOU.csv   CBDG.csv   CGWN.csv   CPSL.csv   CXIJ.csv   
CXQX.csv   CXYL.csv   DBQH.csv   DIJR.csv   DRDQ.csv   DXJP.csv   
EGRU.csv   EMBJ.csv   EODT.csv   EUDK.csv   FAFH.csv   FGTV.csv   
FIVC.csv   FJEB.csv   FMKJ.csv   FMRE.csv   FPIT.csv   FQGS.csv   
FQMM.csv   FVZI.csv   FWDA.csv   FWVY.csv   FXXV.csv   GCIV.csv   
GGMO.csv   GGWU.csv   GJJJ.csv   GZTO.csv   HASK.csv   HCWV.csv   
HDNQ.csv   HIXM.csv   HRGF.csv   HTLW.csv   IHGX.csv   IIMV.csv   
IQMQ.csv   ITCT.csv   IXRA.csv   JBXP.csv   JKOY.csv   JVRV.csv   
JYVB.csv   KRKM.csv   KSQU.csv   LAWW.csv   LCPU.csv   LMUU.csv   
LQKJ.csv   LVEY.csv   MCCO.csv   MHGM.csv   MPOB.csv   MRPD.csv   
MTXB.csv   NGVO.csv   NUAO.csv   ODJH.csv   OGBK.csv   ONVA.csv   
OUWM.csv   OVOW.csv   OWHE.csv   PGBB.csv   PGJC.csv   QHTL.csv   
QMGI.csv   QMUX.csv   QQTV.csv   QVFJ.csv   QZPJ.csv   RCEH.csv   
RGYJ.csv   RIKR.csv   RRSK.csv   RTBV.csv   RTUG.csv   RVQO.csv   
SFUG.csv   SGLD.csv   SIUT.csv   SSNK.csv   SSXP.csv   TEYQ.csv   
TMPJ.csv   TRTT.csv   TRUK.csv   TWBG.csv   TYJR.csv   UFNF.csv   
UICN.csv   UING.csv   UPGW.csv   UREH.csv   URXR.csv   UVRZ.csv   
UZMT.csv   VAGY.csv   VCVG.csv   VJGB.csv   VKPD.csv   VNWM.csv   
VPQA.csv   VZYX.csv   WFKT.csv   WGNY.csv   WJJU.csv   WMKQ.csv   
WOKD.csv   WONG.csv   WRED.csv   WTIY.csv   XBCP.csv   XKAL.csv   
XPRU.csv   XQJO.csv   YFDE.csv   YJKM.csv   YLTR.csv   YNRZ.csv   
YPGZ.csv   YPQL.csv   YYTZ.csv   ZDGH.csv   ZTAL.csv
```

</details>

---

# 📋 Subject Processing Status

Documentation of how each subject's data was processed from the raw experimental files.

## Status Codes

| Code | Icon | Meaning |
|------|------|---------|
| **V** / **Y** | ✅ | Data parsed perfectly by the algorithm |
| **N** | 🔄 | Required hardcoded 10-minute shift (algorithm found training maze) |
| **X** | ❌ | Data discarded (visual made no sense even after adjustment) |

---

## 🏷️ Labeled Data

<details>
<summary>Click to expand (94 subjects)</summary>

| Subject | Status | Notes |
|---------|--------|-------|
| IZZO | ❌ | |
| SVBB | ❌ | |
| RCEH | 🔄 | |
| VUUK | ❌ | |
| IXRA | 🔄 | |
| FMVE Bad | ❌ | |
| CXIJ | 🔄 | |
| DKAF | ❌ | |
| RTUG | ✅ | |
| CPSL | ✅ | |
| JHMW | ❌ | |
| NWTC | ❌ | |
| YBRX | ❌ | |
| MLOS | ❌ | |
| KMRY | ❌ | |
| CDYY | ❌ | |
| LQKJ | ✅ | |
| AOXY | 🔄 | |
| WGNY | ✅ | |
| UVRZ | 🔄 | |
| OGTB | 🔄 | |
| BPPX | 🔄 | |
| GJJJ | 🔄 | |
| YFDE | 🔄 | |
| RIKR | 🔄 | |
| YJKM | 🔄 | |
| XLLZ | ❌ | |
| UNWN | ❌ | |
| VPQA | 🔄 | |
| MPOB | 🔄 | |
| UPCV | ❌ | |
| OUWM | 🔄 | |
| JBXP | 🔄 | |
| VZYX | 🔄 | |
| RSXQ | ❌ | |
| YPQL | 🔄 | |
| WMKQ | 🔄 | |
| HASK | 🔄 | |
| UFNF | 🔄 | |
| IHGX | 🔄 | |
| TMPJ | 🔄 | |
| ZTAL | 🔄 | |
| VNWM | 🔄 | |
| ODJH | 🔄 | |
| SIUT | 🔄 | |
| XLZQ | ❌ | |
| DRDQ | 🔄 | |
| FXXV | 🔄 | |
| EGRU | 🔄 | |
| ZDGH | 🔄 | |
| TEYQ | 🔄 | |
| VKPD | 🔄 | |
| TYJR | 🔄 | |
| YNRZ | 🔄 | |
| RGYJ | 🔄 | |
| ANAV | 🔄 | |
| URXR | 🔄 | |
| NGVO | 🔄 | |
| QQTV | 🔄 | |
| RTBV | 🔄 | |
| OWHE | 🔄 | |
| QVFJ | 🔄 | |
| CGWN | 🔄 | |
| LAWW | 🔄 | |
| BVEH | 🔄 | |
| DXJP | 🔄 | |
| PGBB | 🔄 | |
| MRPD | 🔄 | |
| JVRV | 🔄 | |
| MTXB | 🔄 | |
| KSQU | 🔄 | 2 candidates |
| NUAO | 🔄 | |
| FWPA | ✅ | 2 candidates |
| CXQX | 🔄 | |
| EOPT | 🔄 | |
| OGBK | 🔄 | |
| WTIY | 🔄 | |
| GZTO | 🔄 | |
| EUDK | 🔄 | |
| GQYU | ❌ | 2 candidates |
| UPGW | 🔄 | |
| SSNK | 🔄 | 2 candidates |
| IQMQ | 🔄 | |
| GGWU | 🔄 | |
| DBQH | 🔄 | |
| ZDNA | ❌ | |
| YYTZ | 🔄 | 2 candidates |
| XQJO | 🔄 | |
| UICN | 🔄 | |
| HRGF | 🔄 | |
| ONVA | 🔄 | |
| TWJS | ❌ | 2 candidates |
| WONG | 🔄 | |
| MCCO | 🔄 | |

</details>

---

## 🔓 Unlabeled Data

<details>
<summary>Click to expand (81 subjects)</summary>

| Subject | Status | Notes |
|---------|--------|-------|
| AAAA | 🔄 | |
| ACGN | 🔄 | |
| AELV | 🔄 | |
| BBBB | ❌ | |
| BBHD | ✅ | |
| BFFT | ✅ | |
| BFJK | 🔄 | |
| BPUF | ✅ | |
| BQHT | 🔄 | |
| BWNF | ✅ | |
| BYOU | 🔄 | |
| CBDG | 🔄 | |
| CFLN | ❌ | |
| CXYL | ✅ | |
| DIJR | ✅ | |
| EMBJ | 🔄 | |
| FAFH | ✅ | |
| FGTV | 🔄 | 2 candidates |
| FIVC | 🔄 | |
| FJAJ | ❌ | |
| FJEB | ✅ | |
| FMKJ | 🔄 | |
| FMRE | 🔄 | |
| FPIT | 🔄 | |
| FQGS | 🔄 | |
| FQMM | ✅ | |
| FVZI | ✅ | |
| FWVY | ✅ | |
| GCIV | ✅ | |
| GGMO | 🔄 | |
| HCWV | ✅ | |
| HDNQ | ✅ | |
| HIXM | ✅ | |
| HTLW | 🔄 | |
| IAHA | ❌ | |
| IIMV | ✅ | |
| ITCT | ✅ | |
| JKOY | ✅ | |
| JYVB | ✅ | |
| KRKM | 🔄 | |
| KXKS | 🔄 | |
| LCPU | ✅ | |
| LFWZ | 🔄 | |
| LMUU | ✅ | |
| LVEY | ✅ | |
| MEPW | ❌ | |
| MHGM | ✅ | |
| NEQV | ❌ | |
| OVOW | 🔄 | |
| PGJC | 🔄 | |
| QHTL | 🔄 | |
| QKVF | ❌ | |
| QMGI | 🔄 | |
| QMUX | ✅ | |
| QZPJ | ✅ | |
| RRSK | ✅ | |
| RVQO | 🔄 | |
| SFUG | 🔄 | |
| SGLD | 🔄 | |
| SSXP | ✅ | |
| test | — | Test file |
| TRTT | ✅ | |
| TRUK | ✅ | |
| TWBG | ✅ | |
| UING | 🔄 | |
| UREH | 🔄 | |
| UZMT | 🔄 | |
| VAGY | ✅ | |
| VCVG | ✅ | |
| VJGB | ✅ | |
| WFKT | ✅ | |
| WJJU | 🔄 | |
| WOKD | 🔄 | |
| WRED | ✅ | |
| WTYX | ❌ | |
| XBCP | ✅ | |
| XKAL | 🔄 | |
| XPRU | 🔄 | |
| YDJH | ❌ | |
| YLTR | ✅ | |
| YPGZ | 🔄 | |

</details>

---

<p align="center">
  <a href="../README.md">⬅️ Back to Main README</a>
</p>
