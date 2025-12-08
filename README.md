>**If you have any questions regarding this repository, please contact Ruida Zeng at ruida dot zeng at vanderbilt dot edu**

## Cluster Analysis on Subject Data in Immersive Virtual Environments
This repository contains my work from the 2019 VUSE undergraduate summer research program, at the ***Learning in Virtual Environments (LIVE)*** research lab at [Vanderbilt University's School of Engineering](https://engineering.vanderbilt.edu). The graduate research assistant for this project is Richard Paris, who is responsible for the creation of the immersive virtual environments using Unity, and promptly conducted the experiments on around 200 subjects. The primary investigator for the project is [Dr. Bobby Bodenheimer](https://engineering.vanderbilt.edu/bio/robert-bodenheimer), associate professor at the [Department of Electrical Engineering and Computer Science](https://engineering.vanderbilt.edu/eecs/).

It mainly consists of 143 parsed `.csv` files in the "Parsed Data" sub-folder and several machine learning source codes with a detailed explanation on the methodology attempted. I also included an [appendix](#appendix), which contains useful information regarding the raw data and the parsed data.

**Note**: *Future research, either through a variety machine learning algorithms or otherwise, is encouraged on the 143, nicely parsed, `.csv` files containing information of the maze.*

***Python modules required to be installed: numpy, pandas, sklearn, matplotlib and their dependencies.***

### Project Structure

```
vr-navigation/
├── clustering/              # K-means clustering scripts
│   ├── km_linear.py
│   ├── km_quadruple.py
│   ├── km_vector.py
│   ├── km_vector_more.py
│   ├── km_color.py
│   ├── km_color_more.py
│   ├── km_3d.py
│   ├── km_avg.py
│   └── failed_km.py
├── visualization/           # Visualization scripts
│   ├── visual.py
│   ├── turtle_viz.py
│   ├── color_single.py
│   └── color_double.py
├── preprocessing/           # Data parsing scripts (legacy)
│   ├── makecsv.py
│   ├── matplotfullalgo.py
│   ├── subdir.py
│   ├── subdir_multiple.py
│   └── subdir_unique.py
├── Parsed Data/             # 143 parsed CSV files
└── Resources/               # Images and documentation
```

### Parsed Data
The attributes of the parsed `.csv` files are `date/time`, `seconds since started`, `posX`, `posY`, `posZ`, `rotX`, `rotY`, `rotZ`, respectively. The raw tab-separated `.txt` files before parsing contained more unimportant attributes but was sliced.

---

## Visualization Scripts

#### `visualization/color_single.py`
Visual representation of one singular `.csv` file using matplotlib module based on the temporal attributes, with red indicates early and blue indicates late.

![one color](/Resources/1color.png)

#### `visualization/color_double.py`
Visual representation of two `.csv` files using matplotlib module based on the temporal attributes, with red indicates early and blue indicates late.

![two color](/Resources/2color.png)

#### `visualization/visual.py`
Visual representation using matplotlib module.

![visual plot](/Resources/visual.png)

#### `visualization/turtle_viz.py`
Visual representation using turtle module (live animation).

![turtle plot](/Resources/turtle.png)

---

## Clustering Scripts

#### `clustering/failed_km.py`
Failed attempt at k-means clustering all (posX, posZ) in tuple forms in a numpy array, from 5 distinct pandas dataframes which were imported from the first 5 parsed data alphabetically. Returned `ValueError: Found array with dim 3. Estimator expected <= 2`. Kept for educational purposes.

#### `clustering/km_3d.py`
Temporal attribute (time) is added as the Z-axis for 3D visual representation of the clusters.

![k-means 3d](/Resources/km_3d.png)

#### `clustering/km_avg.py`
A 3D representation, with time as the Z-axis, of the average (mean) position of the clusters.

![k-means average](/Resources/km_avg.png)

#### `clustering/km_linear.py`
Successful k-means clustering on (posX, posZ) tuples on a subject dataframe, imported from a singular parsed data file. In this example, I set the number of clusters to 8 for `AAAA.csv`, but they can be easily modified.

![k-means linear plot](/Resources/km_linear.png)

#### `clustering/km_quadruple.py`
Traverse through all `.csv` files in the Parsed Data folder.
Successful k-means clustering on (posX, posZ) tuples on each subject dataframe from all parsed data file. The quadruples are calculated from time spent around the vicinity of 4 decision points (intersections) in the maze.

![k-means quadruple plot](/Resources/km_quadruple.png)

#### `clustering/km_vector.py`
Successful k-means clustering on decimated posY stacked on top of posX, forming a vector for each of the subject dataframe from all parsed data files. Since the codes require uniformity of vector size, we had to slice out 2 data files because of the particular decimation.

![k-means vector plot](/Resources/km_vector.png)

#### `clustering/km_vector_more.py`
Successful k-means clustering on "less" decimated posY stacked on top of posX, forming a vector for each of the subject dataframe from all parsed data files. Since the codes require uniformity of vector size, we had to slice out 39 data files because of the particular decimation.

![k-means vector more plot](/Resources/km_vector_more.png)

#### `clustering/km_color.py`
Successful k-means clustering on decimated posY stacked on top of posX, forming a vector for each of the subject dataframe from all parsed data files. Since the codes require uniformity of vector size, we had to slice out 2 data files because of the particular decimation. The graphs are coded with the temporal attributes, with red indicates early and blue indicates late.

![k-means color plot](/Resources/km_color.png)

#### `clustering/km_color_more.py`
Successful k-means clustering on "less" decimated posY stacked on top of posX, forming a vector for each of the subject dataframe from all parsed data files. Since the codes require uniformity of vector size, we had to slice out 39 data files because of the particular decimation. The graphs are coded with the temporal attributes, with red indicates early and blue indicates late.

![k-means color more plot](/Resources/km_color_more.png)

---

## Preprocessing Scripts (Legacy)

These scripts require the original raw experimental data files which are not included in this repository. They will display helpful error messages if run without the required data.

#### `preprocessing/makecsv.py`
This source code generates a `.csv` file from the original, tab-separated, `.txt` file by applying my "find 10 min" slicing algorithm.

#### `preprocessing/matplotfullalgo.py`
Returns a visual representation using matplotlib module of a 10 minutes slot found by my "find 10 min" slicing algorithm. This visual is used to determine whether or not my algorithm has found the correct 10 minutes.

#### `preprocessing/subdir.py`
This is the code I applied on the original, raw, data in order to find the 10 minutes of useful data. However, since this piece of "find 10 min" algorithm does not work on all files, I wrote this script to iterate through every original raw data file to determine the efficiency of my algorithms.

#### `preprocessing/subdir_multiple.py`
This is a modification on the `subdir.py`, such that it will tell me which are the files that my "find 10 min" slicing algorithm found ***two or more*** candidates.

#### `preprocessing/subdir_unique.py`
This is a modification on the `subdir.py`, such that it will tell me which are the files that my "find 10 min" slicing algorithm found ***only one*** candidate.

---

### Appendix
I prepared a poster presentation for 2019 Vanderbilt School of Engineering Summer Undergraduate Research Experience Program as 2019 Summer Research Fellow.

![poster presentation](/Resources/poster.jpg)

 
The following tables contain the manuever I had to apply based on the graphic representation given by applying `preprocessing/matplotfullalgo.py` to each individual raw data, which is significantly larger, containing more unuseful data.

**`Y`** indicates that the data was parsed out perfectly, **`N`** indicates that I hardcoded a shift of 10 minutes because the visual gave us a visual representation of the training maze which procedes the learning maze, and **`X`** indicates throwing out the data completely because the visual made no sense even after hardcoded tinkering.

| Subject ID      | Status | Additional Notes | 
|-----------------|--------|------------------| 
| ***LABELED DATA***    |        |                  | 
| IZZO            | X      |                  | 
| SVBB            | X      |                  | 
| RCEH            | N      |                  | 
| VUUK            | X      |                  | 
| IXRA            | N      |                  | 
| FMVE Bad        | X      |                  | 
| CXIJ            | N      |                  | 
| DKAF            | X      |                  | 
| RTUG            | V      |                  | 
| CPSL            | V      |                  | 
| JHMW            | X      |                  | 
| NWTC            | X      |                  | 
| YBRX            | X      |                  | 
| MLOS            | X      |                  | 
| KMRY            | X      |                  | 
| CDYY            | X      |                  | 
| LQKJ            | V      |                  | 
| AOXY            | N      |                  | 
| WGNY            | V      |                  | 
| UVRZ            | N      |                  | 
| OGTB            | N      |                  | 
| BPPX            | N      |                  | 
| GJJJ            | N      |                  | 
| YFDE            | N      |                  | 
| RIKR            | N      |                  | 
| YJKM            | N      |                  | 
| XLLZ            | X      |                  | 
| UNWN            | X      |                  | 
| VPQA            | N      |                  | 
| MPOB            | N      |                  | 
| UPCV            | X      |                  | 
| OUWM            | N      |                  | 
| JBXP            | N      |                  | 
| VZYX            | N      |                  | 
| RSXQ            | X      |                  | 
| YPQL            | N      |                  | 
| WMKQ            | N      |                  | 
| HASK            | N      |                  | 
| UFNF            | N      |                  | 
| IHGX            | N      |                  | 
| TMPJ            | N      |                  | 
| ZTAL            | N      |                  | 
| VNWM            | N      |                  | 
| ODJH            | N      |                  | 
| SIUT            | N      |                  | 
| XLZQ            | X      |                  | 
| DRDQ            | N      |                  | 
| FXXV            | N      |                  | 
| EGRU            | N      |                  | 
| ZDGH            | N      |                  | 
| TEYQ            | N      |                  | 
| VKPD            | N      |                  | 
| TYJR            | N      |                  | 
| YNRZ            | N      |                  | 
| RGYJ            | N      |                  | 
| ANAV            | N      |                  | 
| URXR            | N      |                  | 
| NGVO            | N      |                  | 
| QQTV            | N      |                  | 
| RTBV            | N      |                  | 
| OWHE            | N      |                  | 
| QVFJ            | N      |                  | 
| CGWN            | N      |                  | 
| LAWW            | N      |                  | 
| BVEH            | N      |                  | 
| DXJP            | N      |                  | 
| PGBB            | N      |                  | 
| MRPD            | N      |                  | 
| JVRV            | N      |                  | 
| MTXB            | N      |                  | 
| KSQU            | N      | 2 candidates     | 
| NUAO            | N      |                  | 
| FWPA            | V      | 2 candidates     | 
| CXQX            | N      |                  | 
| EOPT            | N      |                  | 
| OGBK            | N      |                  | 
| WTIY            | N      |                  | 
| GZTO            | N      |                  | 
| EUDK            | N      |                  | 
| GQYU            | X      | 2 candidates     | 
| UPGW            | N      |                  | 
| SSNK            | N      | 2 candidates     | 
| IQMQ            | N      |                  | 
| GGWU            | N      |                  | 
| DBQH            | N      |                  | 
| ZDNA            | X      |                  | 
| YYTZ            | N      | 2 candidates     | 
| XQJO            | N      |                  | 
| UICN            | N      |                  | 
| HRGF            | N      |                  | 
| ONVA            | N      |                  | 
| TWJS            | X      | 2 candidates     | 
| WONG            | N      |                  | 
| MCCO            | N      |                  | 
| ***UNLABELED DATA*** |        |                  | 
| AAAA            | N      |                  | 
| ACGN            | N      |                  | 
| AELV            | N      |                  | 
| BBBB            | X      |                  | 
| BBHD            | V      |                  | 
| BFFT            | V      |                  | 
| BFJK            | N      |                  | 
| BPUF            | V      |                  | 
| BQHT            | N      |                  | 
| BWNF            | V      |                  | 
| BYOU            | N      |                  | 
| CBDG            | N      |                  | 
| CFLN            | X      |                  | 
| CXYL            | V      |                  | 
| DIJR            | V      |                  | 
| EMBJ            | N      |                  | 
| FAFH            | V      |                  | 
| FGTV            | N      | 2 candidates     | 
| FIVC            | N      |                  | 
| FJAJ            | X      |                  | 
| FJEB            | V      |                  | 
| FMKJ            | N      |                  | 
| FMRE            | N      |                  | 
| FPIT            | N      |                  | 
| FQGS            | N      |                  | 
| FQMM            | V      |                  | 
| FVZI            | V      |                  | 
| FWVY            | V      |                  | 
| GCIV            | V      |                  | 
| GGMO            | N      |                  | 
| HCWV            | V      |                  | 
| HDNQ            | V      |                  | 
| HIXM            | V      |                  | 
| HTLW            | N      |                  | 
| IAHA            | X      |                  | 
| IIMV            | V      |                  | 
| ITCT            | V      |                  | 
| JKOY            | V      |                  | 
| JYVB            | V      |                  | 
| KRKM            | N      |                  | 
| KXKS            | N      |                  | 
| LCPU            | V      |                  | 
| LFWZ            | N      |                  | 
| LMUU            | V      |                  | 
| LVEY            | V      |                  | 
| MEPW            | X      |                  | 
| MHGM            | V      |                  | 
| NEQV            | X      |                  | 
| OVOW            | N      |                  | 
| PGJC            | N      |                  | 
| QHTL            | N      |                  | 
| QKVF            | X      |                  | 
| QMGI            | N      |                  | 
| QMUX            | V      |                  | 
| QZPJ            | V      |                  | 
| RRSK            | V      |                  | 
| RVQO            | N      |                  | 
| SFUG            | N      |                  | 
| SGLD            | N      |                  | 
| SSXP            | V      |                  | 
| test            | ROFL   |                  | 
| TRTT            | V      |                  | 
| TRUK            | V      |                  | 
| TWBG            | V      |                  | 
| UING            | N      |                  | 
| UREH            | N      |                  | 
| UZMT            | N      |                  | 
| VAGY            | V      |                  | 
| VCVG            | V      |                  | 
| VJGB            | V      |                  | 
| WFKT            | V      |                  | 
| WJJU            | N      |                  | 
| WOKD            | N      |                  | 
| WRED            | V      |                  | 
| WTYX            | X      |                  | 
| XBCP            | V      |                  | 
| XKAL            | N      |                  | 
| XPRU            | N      |                  | 
| YDJH            | X      |                  | 
| YLTR            | V      |                  | 
| YPGZ            | N      |                  | 
