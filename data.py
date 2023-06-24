import os
import torch
import torch_geometric as pyg
import numpy as np
import networkx as nx
from utils import load_pickle


class GraphDataset(torch.utils.data.Dataset):
    """
    Graph Dataset. Collects NetworkX graph from a pre-defined folder and
    transforms them to Pytorch Geometric (pyg.data.Data()) instances.
    """
    def __init__(self, path, graph_type = 'zoning'):
        self.graph_path = os.path.join(path, 'graph_in' if 'zoning' in graph_type else 'graph_out')
        self.struct_path = os.path.join(path, 'struct_in')
        self.full_path = os.path.join(path, 'full_out')

        # include graph transformations if you like
        # self.graph_transform = graph_transform

    def __getitem__(self, index):

        # get access graph (name is index)
        graph_nx = load_pickle(os.path.join(self.graph_path, f'{index}.pickle'))

        # add images as graph attributes
        struct = np.load(os.path.join(self.struct_path, f'{index}.npy'))
        full = np.load(os.path.join(self.full_path, f'{index}.npy'))
        graph_nx.graph['struct'] = struct[np.newaxis, ...]
        graph_nx.graph['full'] = full[np.newaxis, ...]

        # transform networkx graph to pytorch geometric graph
        graph_pyg = pyg.utils.from_networkx(graph_nx)

        # transform graph if you like
        # graph_pyg = self.graph_transform(graph_pyg)

        return graph_pyg

    def __len__(self):
        return len(os.listdir(self.graph_path))
