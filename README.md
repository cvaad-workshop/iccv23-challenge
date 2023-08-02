# Floor Plan Auto-Completion at Scale
We present this year's workshop challenge: **Floor Plan Auto-Completion at Scale**.

The task of floor plan auto-completion involves generating a complete floor plan configuration based on a building's necessary structural elements, and a set of user-defined constraints organized in a graph structure. The main objective is to develop deep learning models that learn the relationship between the graph-structured requirements and structural components (right side of the image) and the configuration of the entire floor plan (left side of the image):

![fp-auto-completion](https://github.com/cvaad-workshop/iccv23-challenge/assets/40263235/b5f96e97-ad38-4e14-8270-7dcb337575e4)

This challenge presents an opportunity to delve into **deep learning research that focuses on generating floor plans at the scale of the building**, an area of research that remains largely unexplored in the field of computer science. Even though we expect that current state-of-the-art approaches for floor plan generation of single-unit apartment are a promising starting point, scaling will bring many new and exciting challenges. Hence, the task asks for rethinking the current neural model architectures and training strategies for floor plan generation. 

We hope that this challenge will inspire numerous researchers world-wide.

## Data
We developed our own dataset for the challenge; **Modified Swiss Dwellings: a Machine Learning-ready Dataset for Floor Plan Auto-Completion at Scale** (MSD):

- [Link to dataset and download @ Kaggle](https://www.kaggle.com/datasets/caspervanengelenburg/modified-swiss-dwellings);
- Based on the [Swiss Dwellings](https://zenodo.org/record/7788422) database;
- Contains **5000+ floor plans** of single- as well as multi-unit building complexes.

Most importantly, MSD extends the scale of the building, namely to multi-unit building complexes, w.r.t. other well know floor plan datasets like [RPLAN](http://staff.ustc.edu.cn/~fuxm/projects/DeepLayout/index.html).

### Folder structure
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

[This is a link to how the data is formatted](https://github.com/cvaad-workshop/iccv23-challenge/blob/main/data-README.md).

## Awards
We have a reward of 1000 EUR (~1.095 USD) for the best contender. 

## Evaluation

### Codalab
The evaluation is handled automatically in [Codalab](). 

### Metrics
Evaluation will be done by the (mean) Intersection-over-Union between the predicted full floor plan and the ground truth:

$$ \text{mIOU} = \frac{1}{N_A} \sum_{c=1}^{N_A} \text{IoU} \left( A==c, B==c\right).$$

We have four measures that contain different subsets of the classes in the evaluations:

1. **mIOU w/o background**: all classes except for the background;
2. **mIOU w/ background**: all classes;
3. **mIOU structure only**: only the "structure" class;
4. A weighted sum of (1), (2), and (3): $\frac{2*\text{(1)} + 1*\text{(2)} + 5*\text{(3)}}{8}$.

The weighted sum (4) determines the overall quantitative score of the submission.

\[**IMPORTANT -- QUALITATIVE EVALUATION**\]
In addition, the submissions of the top contenders will be checked by a team of practicing architects on 1) architectural quality and 2) whether or not they satisfactorily comply to the imposed (graph-structured) requirements. 

Effectively, it means that the top-ranked contender on the leaderboard is not necessarily the winner of the competition. We will reveal the winner before the workshop. 

## Submission
Your submission should be packed as a **ZIPPED folder containing all predicted full floor plan configurations as IMAGES**. (The folder can be named to your liking.) Images should have the following properties:

- **size**: **512 x 512**;
- **compression technique**: **PNG**;
- **naming**: based on the naming in the test set, *e.g.*, "4167.png".

Furthermore, there are two very important properties that (if you want your submission to have a maximal score) the images should have:

\[**IMPORTANT 1 -- POSITIONING**\]
The floor plan should be correctly **positioned** in the image (!!). This means that the real location of a pixel should align with the location provided in the `struct_in` folder of the test set. The locations of the pixels are in the 2nd and 3rd channel of the corresponding `.npy` arrays. The locations (xs and ys) are extracted as follows:

```python
# Define path
path_struct = r'C:\Users\caspervanengel\OneDrive\Documents\PHD\1_data\swiss-dwellings\3.0.0\cvaad-challenge\test\struct_in'  # change this to your own path (!)

# Load structural components (as 3D array)
stack = np.load(os.path.join(path_struct, f'{id}.npy'))

# Get structural component as binary map
struct = stack[..., 0].astype(np.uint8)  # structure as 2D (int) array

# Important part here: GET LOCATIONS OF ALL PIXELS
xs = stack[..., 1]  # x-locations as 2D (float) array
ys = stack[..., 2]  # y-locations as 2D (float) array
```

\[**IMPORTANT 2 -- CLASS LABELS**\]
The floor plan images should have the **correct pixel values**: pixels should corresponds to the correct classes. The range of classes is given here:

```python
{'Bedroom': 0,
 'Livingroom': 1,
 'Kitchen': 2,
 'Dining': 3,
 'Corridor': 4,
 'Stairs': 5,
 'Storeroom': 6,
 'Bathroom': 7,
 'Balcony': 8,
 'Structure': 9,
 'Background': 13}
```

For more information on how you should pack your submission and save your predictions see "Resources" below.

## Resources
To accommodate submissions to the challenge we provide a toolkit that contains:
- [Python tools for handling (loading, understanding, and converting) the data](https://github.com/cvaad-workshop/iccv23-challenge/blob/main/guidelines.ipynb); and 
- [Python tools for helping to create the correct submissions](https://github.com/cvaad-workshop/iccv23-challenge/blob/main/submission.ipynb).

## Important Dates
- Data and description open: June 22nd, 2023;
- Challenges open: July 10th, 2023;
- Challenges close: September 15th, 2023;
- One-pager (or poster) due: September 20th, 2023;
- Winners announced: Live session at ICCV.

## Rules
- For submissions on CodaLab to qualify to the challenge we require the contenders to submit a short **technical report** about their final submission. See details below under “Report”. Submissions without a report associated do not qualify to the competition.
- Top contenders in the challenge are required to make their work **reproducible**. This means that contenders should be able to share their code (or show to others how it can be used) and that the results are equivalent to the scores in the leaderboard. The organizers might (randomly) contact top contenders to check this criteria. (It is not required, although highly encouraged, to provide a GitHub repository, or similar, about the submission.)
- Organizers retain the right to disqualify any submissions that violate these rules.
- (Be aware that you are allowed to use any other data for training or any pre-trained model.)

## Report
- For submissions on CodaLab to qualify to the challenge we require the authors submit a short **technical report** about their final submission.
- We suggest that the technical report consists of three sections: introduction, method, and results/discussion.
- The report should not be longer than 3 pages and shouldn't extend 2000 words.
- Authors are to submit their report to [ArXiv](https://arxiv.org/) and submit the link to c.c.j.vanengelenburg AT tudelft DOT nl. Those unable to submit to Arxiv can email their report directly to c.c.j.vanengelenburg AT tudelft DOT nl.
- After the conference we will publish the links to the technical reports on the workshop website.
