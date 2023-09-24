class Status:
    TRAIN = 'train'
    DEV = 'dev'
    TEST = 'test'


class Setting:
    # device
    device = None
    status = None
    simple_dev = False
    fast_eval = False

    # pad
    UNSET = -1

    # dataset
    dataset = None
