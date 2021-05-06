from mock_data.seed import mongo_client

db = mongo_client()


def root():
    all = db.get_all_collections()
    for name in all:
        collection = all[name]
        rows = collection.get_all_rows()
        for row in rows:
            print(rows[row])

root()


def clients():
    return json_util.dumps(db.clients.find({}))


def clients_by_id(client_id):
    client_object_id = ObjectId(client_id)
    return json_util.dumps(db.clients.find_one({'_id': client_object_id}))


def engagements():
    return json_util.dumps(db.engagements.find({}))


def engagements_by_id(engagement_id):
    engagement_object_id = ObjectId(engagement_id)
    return json_util.dumps(db.engagements.find_one({'_id': engagement_object_id}))


def interactions():
    # TODO: Modify this endpoint according to problem statement!
    return json_util.dumps(db.interactions.find({}))


def interactions_by_id(interaction_id):
    interaction_object_id = ObjectId(interaction_id)
    return json_util.dumps(db.interactions.find_one({'_id': interaction_object_id}))


