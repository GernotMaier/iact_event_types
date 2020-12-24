import argparse
from pathlib import Path
import event_classes

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description=(
            'An example script how to load trained models.'
            'Remember not to use the data used to train these models.'
            'In future perhaps also the test data will be saved.'
        )
    )

    args = parser.parse_args()

    labels = 'log_ang_diff'
    train_features = [
        'log_reco_energy',
        'log_NTels_reco',
        'array_distance',
        'img2_ang',
        'log_SizeSecondMax',
        'MSCW',
        'MSCL',
        'log_EChi2S',
        'log_av_size'
    ]

    trained_models = event_classes.load_models(['linear_regression'])
    dtf_e_test = event_classes.load_test_dtf()

    Path('plots').mkdir(parents=True, exist_ok=True)

    for this_trained_model_name, this_trained_model in trained_models.items():
        plt = event_classes.plot_test_vs_predict(
            dtf_e_test,
            this_trained_model,
            this_trained_model_name,
            train_features,
            labels
        )

        plt.savefig('plots/{}.pdf'.format(this_trained_model_name))