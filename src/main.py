import pdb
import argparse

from prescience import make_prediction, resolve_predictions, view_stats, import_data

def main():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command')

    predict_parser = subparser.add_parser('predict', help='Make a prediction')
    predict_parser.add_argument('-e', '--event', type=str, required=True, help='Prediction event')
    predict_parser.add_argument('-p', '--prediction', type=float, required=True, help='0.0-100.0 likelihood of event')
    predict_parser.add_argument('-d', '--result_date', type=str, required=True, help='ISO date when the outcome of event will be known')
    predict_parser.add_argument('-t', '--tags', nargs='+', type=str, help='Optional tags')

    resolve_parser = subparser.add_parser('resolve', help='Resolve pending predictions')
    stats_parser = subparser.add_parser('stats', help='View stats')

    import_parser = subparser.add_parser('import', help='Load csv')
    import_parser.add_argument('filename', help="csv file to import")


    args = parser.parse_args()

    if args.command == 'predict':
        make_prediction(**vars(args))

    if args.command == 'resolve':
        resolve_predictions(**vars(args))

    if args.command == 'stats':
        view_stats(**vars(args))

    if args.command == 'load':
        import_data(args.filename)

if __name__ == '__main__':
    main()
