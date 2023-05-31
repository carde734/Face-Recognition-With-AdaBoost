
def WeakClassifier(T, P, X):
    """ WEAKCLASSIFIER
    Classify images using a decision stump.
    Takes a vector X of scalars obtained by applying one Haar feature to all
    training images. Classifies the examples using a decision stump with
    cut-off T and polarity P. Returns a vector C of classifications for all
    examples in X.

    You are not allowed to use a loop in this function.
    This is for your own benefit, since a loop will be too slow to use
    with a reasonable amount of Haar features and training images.
    """
    if P==1:
        C=[1 if Xi >= T else -1 for Xi in X ]
    elif P==-1:
        C=[1 if Xi <= T else -1 for Xi in X ]

    return C


def WeakClassifierError(C, D, Y):
    """ WEAKCLASSIFIERERROR
    Calculate the error of a single decision stump.
    Takes a vector C of classifications from a weak classifier, a vector D
    with weights for each example, and a vector Y with desired
    classifications. Calculates the weighted error of C, using the 0-1 cost
    function.

    You are not allowed to use a loop in this function.
    This is for your own benefit, since a loop will be too slow to use
    with a reasonable amount of Haar features and training images.
    """
    import numpy as np
    
    NotEqual=(np.not_equal(Y, C)).astype(int)
    Errors = NotEqual * D
    E =sum(Errors)

    return E