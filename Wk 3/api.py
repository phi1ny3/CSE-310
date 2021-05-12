import numpy as np
import pandas as pd
import datetime as dt
from sklearn.cluster import DBSCAN
from flask import Flask, request, jsonify

app = Flask(__name__)


def get_infected_names(input_name):

    df = pd.read_json('data.json')

    epsilon = 0.0018288 # a radial distance of 6 feet in kilometers
    model = DBSCAN(eps=epsilon, min_samples=2, metric='haversine').fit(df[['latitude', 'longitude']])
    df['cluster'] = model.labels_.tolist()

    input_name_clusters = []
    for i in range(len(df)):
        if df['id'][i] == input_name:
            if df['cluster'][i] in input_name_clusters:
                pass
            else:
                input_name_clusters.append(df['cluster'][i])
    
    infected_names = []
    for cluster in input_name_clusters:
        if cluster != -1:
            ids_in_cluster = df.loc[df['cluster'] == cluster, 'id']
            for i in range(len(ids_in_cluster)):
                member_id = ids_in_cluster.iloc[i]
                if (member_id not in infected_names) and (member_id != input_name):
                    infected_names.append(member_id)
                else:
                    pass
    
    return infected_names

@app.route('/get_infected')
def get_infected():
    input_name = request.args.get('input_name')
    infected_names = get_infected_names(input_name)
    return jsonify({"infected_names": infected_names})

if __name__ == '__main__':
    app.run(debug=True)