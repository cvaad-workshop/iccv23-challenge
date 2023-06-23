# Modified Swiss Dwellings Dataset for Floor Plan Auto-Completion at Scale

We present the **Modified Swiss Dwellings** dataset, a ML-ready dataset for floor plan auto-completion at scale. The dataset is derived from the [Swiss Dwellings database](https://zenodo.org/record/7788422) (v3.0.0). 

## About the challenge
The floor plan auto-completion task takes as input the boundary of a building, the structural elements necessary for the building’s structural integrity, and a set of user constraints formalized in a graph structure, with the goal of automatically generating the full floor plan. 

The challenge is to develop a deep-learning model that can learn from the training data (image or graph or both) the mapping between the coarse zoning area to the fine floor plan configuration by means of learning the room shapes and types and the interior walls in between.

While previous research on floor plan generation has mainly focused on the scale of individual apartments, our challenge sets the stage for floor plan generation at a larger scale: the scale of the apartment complex.

### Evaluation

Evaluation will be done by the (mean) Intersection-over-Union between the predicted full floor plan and the ground truth.

## About the dataset
The dataset (train split) contains **4167 floor plans** of single- as well as multi-unit building complexes, hence extending the building scale w.r.t. of other well know floor plan datasets like [RPLAN](http://staff.ustc.edu.cn/~fuxm/projects/DeepLayout/index.html). 

The dataset can be downloaded from [https://data.4tu.nl/](https://data.4tu.nl/ "https://data.4tu.nl/").

### Folder structure

```markdown
├── swiss-dwellings
│   ├── v3.0.0
│   │   ├── structure_in
│   │   ├── graph_in
│   │   ├── img_out
│   │   ├── graph_out
```

### Training data

#### Input data

1. Required **structural components** as an image representation
	1. Data format: `.npy`
	2. Type: `numpy` array
	3. Data type: `.float16`
	4. Shape: $[512, 512, 3]$
	5. Info:
		1. 1st channel: **binary mask of structure** (0 = structure, 1 = non-structure)
		2. 2nd channel: **x location** 
		3. 3rd channel: **y location**

![image](https://github.com/cvaad-workshop/swiss-dwelling-private/assets/40263235/94508a5e-1437-4028-a224-80e2985f2bdb)

2. Required **zoning access graph** as a graph representation
	1. Data format: `.pickle` 
	2. Type: `networkx.Graph()`
	3. Nodes are area w/ attributes:
		1. `zoning`: **classification of spatial "zone"** 
	4. Edges are access connectivity w/ attributes:
		1. `connectivity`: **classification of access type**, *e.g.*, "door", "entrance door", "passage"

![image](https://github.com/cvaad-workshop/swiss-dwelling-private/assets/40263235/7332348a-58a3-407b-a011-9431c2677b10)

#### Output data

1. **Full floor plan** as an image representation (excluding doors and openings)
	1. Data format: `.npy`
	2. Type: `numpy` array
	3. Data type: `.float16`
	4. Shape: $[512, 512, 3]$
	5. Info:
		1. 1st channel: **multi-class segmentation mask** (integer value corresponds to certain room-type)
		2. 2nd channel: **x location** 
		3. 3rd channel: **y location**

![image](https://github.com/cvaad-workshop/swiss-dwelling-private/assets/40263235/a54d84ff-b14c-4d9b-b7a5-009e570ca658)

2. **Full room-type access graph** as a graph representation (the topology of zoning and room-type access graph are equivalent!)
	1. Data format: `.pickle` 
	2. Type: `networkx.Graph()`
	3. Nodes are area w/ attributes:
		1. `roomtype`: **classification of room-type**, *e.g.*, "Bathroom", "Livingroom", "Bedroom"
		2. `centroid`: **centroid of the room** (midpoint)
		3. `geometry`: **shape of room** as a polygon (`shapely.geometry.Polygon()`)
	4. Edges are access connectivity w/ attributes:
		1. `connectivity`: **classification of access type**, *e.g.*, "door", "entrance door", "passage"

![image](https://github.com/cvaad-workshop/swiss-dwelling-private/assets/40263235/c85259d8-2527-4566-b9da-04c6608eec77)
