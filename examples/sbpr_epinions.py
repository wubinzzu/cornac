# -*- coding: utf-8 -*-

"""
Example for Social Bayesian Personalized Ranking with Epinions dataset

@author: Quoc-Tuan Truong <tuantq.vnu@gmail.com>
"""

import cornac
from cornac.data import Reader, GraphModule
from cornac.datasets import epinions
from cornac.eval_methods import RatioSplit

ratio_split = RatioSplit(data=epinions.load_data(Reader(bin_threshold=4.0)),
                         test_size=0.1, rating_threshold=0.5,
                         exclude_unknowns=True, verbose=True,
                         user_graph=GraphModule(data=epinions.load_trust()))

sbpr = cornac.models.SBPR(k=10, max_iter=50, learning_rate=0.001,
                          lambda_u=0.015, lambda_v=0.025, lambda_b=0.01,
                          verbose=True)
rec_10 = cornac.metrics.Recall(k=10)

cornac.Experiment(eval_method=ratio_split,
                  models=[sbpr],
                  metrics=[rec_10]).run()