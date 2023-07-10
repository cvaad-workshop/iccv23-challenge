# Data
We developed our own dataset for the challenge; **Modified Swiss Dwellings: a Machine Learning-ready Dataset for Floor Plan Auto-Completion at Scale** (MSD):

- [Link to dataset and download @ 4TU.ResearchData](https://data.4tu.nl/datasets/e1d89cb5-6872-48fc-be63-aadd687ee6f9);
- ([Link to dataset and download @ Kaggle](https://www.kaggle.com/datasets/caspervanengelenburg/modified-swiss-dwellings));
- Based on the [Swiss Dwellings](https://zenodo.org/record/7788422) database;
- Contains **5000+ floor plans** of single- as well as multi-unit building complexes.

Most importantly, MSD extends the scale of the building, namely to multi-unit building complexes, w.r.t. other well know floor plan datasets like [RPLAN](http://staff.ustc.edu.cn/~fuxm/projects/DeepLayout/index.html).

## Folder structure
The dataset has two ZIP archives:

- **Training**
```markdown
├── modified-swiss-dwellings-v1-train
│   ├── structure_in
│   ├── graph_in
│   ├── full_out
│   ├── graph_out
```

- **Test** (withheld annotations)
```markdown
├── modified-swiss-dwellings-v1-test
│   ├── structure_in
│   ├── graph_in
```

## Input data

1. Required **structural components** as an image representation
	1. Data format: `.npy`
	2. Type: `numpy` array
	3. Data type: `.float16`
	4. Shape: $[512, 512, 3]$
	5. Info:
		1. 1st channel: **binary mask of structure** (0 = structure, 1 = non-structure)
		2. 2nd channel: **x location** 
		3. 3rd channel: **y location**

2. Required **zoning access graph** as a graph representation
	1. Data format: `.pickle` 
	2. Type: `networkx.Graph()`
	3. Nodes are area w/ attributes:
		1. `zoning`: **classification of spatial "zone"** 
	4. Edges are access connectivity w/ attributes:
		1. `connectivity`: **classification of access type**, *e.g.*, "door", "entrance door", "passage"

## Output data

1. **Full floor plan** as an image representation (excluding doors and openings)
	1. Data format: `.npy`
	2. Type: `numpy` array
	3. Data type: `.float16`
	4. Shape: $[512, 512, 3]$
	5. Info:
		1. 1st channel: **multi-class segmentation mask** (integer value corresponds to certain room-type)
		2. 2nd channel: **x location** 
		3. 3rd channel: **y location**


2. **Full room access graph** as a graph representation (the topology of zoning and room access graph are equivalent!)
	1. Data format: `.pickle` 
	2. Type: `networkx.Graph()`
	3. Nodes are area w/ attributes:
		1. `roomtype`: **classification of room-type**, *e.g.*, "Bathroom", "Livingroom", "Bedroom"
		2. `centroid`: **centroid of the room** (midpoint)
		3. `geometry`: **shape of room** as a polygon (`shapely.geometry.Polygon()`)
	4. Edges are access connectivity w/ attributes:
		1. `connectivity`: **classification of access type**, *e.g.*, "door", "entrance door", "passage"

![image](https://github.com/cvaad-workshop/iccv23-challenge/assets/40263235/91bb134c-9443-471d-992e-e15d3bdca3f0)
fltr: required structural components; zoning access graph; full layout; roomtype access graph.
