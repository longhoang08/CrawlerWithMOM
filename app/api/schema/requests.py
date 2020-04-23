from flask_restplus import fields

crawl_request = {
    'urls': fields.List(fields.String, required=True)
}
