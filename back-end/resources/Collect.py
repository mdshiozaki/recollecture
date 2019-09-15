from flask import request
from flask_restful import Resource
from Model import db, Collect, CollectSchema

collects_schema = CollectSchema(many=True)
collect_schema = CollectSchema()

class CollectResource(Resource):
    def get(self):
        collects = Collect.query.all()
        collects = collects_schema.dump(collects).data
        return {'status': 'success', 'data': collects}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = collect_schema.load(json_data)
        if errors:
            return errors, 422
        category = Collect.query.filter_by(name=data['name']).first()
        if category:
            return {'message': 'Category already exists'}, 400
        category = Collect(
            name=json_data['name'],
            transcript=json_data['transcript'],
            keywords=json_data['keywords']
            )

        db.session.add(category)
        db.session.commit()

        result = collect_schema.dump(category).data

        return { "status": 'success', 'data': result }, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = collect_schema.load(json_data)
        if errors:
            return errors, 422
        category = Collect.query.filter_by(name=data['name']).first()
        if not category:
            return {'message': 'Category does not exist'}, 400
        category.name = data['name']
        category.transcript = data['transcript']
        category.keywords = data['keywords']
        db.session.commit()

        result = collect_schema.dump(category).data

        return { "status": 'success', 'data': result }, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = collect_schema.load(json_data)
        if errors:
            return errors, 422
        category = Collect.query.filter_by(name=data['name']).delete()
        db.session.commit()

        result = collect_schema.dump(category).data

        return { "status": 'success', 'data': result}, 204