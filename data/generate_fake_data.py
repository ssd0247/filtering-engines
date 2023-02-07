def generate_fake_dataset(shape=(500, 25), size=500*25, cols=None, seed=None, dists=None, num_batch_datasets=1):
    """Generate the fake dataset for collaborative filtering task.
    
    Parameters
    ----------
    shape : int, default=(500, 25)
        the shape of the fake dataset (num_rows * num_cols) that are
        going to be generated.
    size : int, default=12500
        the total number of entries that would be in the table.
    cols : List-like, default=None
        the types
    """