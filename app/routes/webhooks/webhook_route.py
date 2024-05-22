from flask import Blueprint, request, make_response
from datetime import datetime
from app.extensions import firebase_handler

webhook_route = Blueprint("webhook", __name__, url_prefix="/webhooks")

@webhook_route.route("/", methods=["POST"])
def gateway():
    try:
        request_data = request.form.to_dict(flat=True)
        form_id = request_data["form[id]"]
        form_name = request_data['form[name]']
        form_fullname_value = request_data['fields[name][raw_value]']
        form_email_value = request_data['fields[email][raw_value]']
        form_message_value = request_data['fields[message][raw_value]']
        form_user_device = request_data['meta[user_agent][value]']
        form_user_ip_address = request_data['meta[remote_ip][value]']

        payload = {
            "form_id": form_id,
            "form_name": form_name,
            "form_fullname_value": form_fullname_value,
            "form_email_value": form_email_value,
            "form_message_value": form_message_value,
            "user_device": form_user_device,
            "user_ipaddress": form_user_ip_address
        }

        firebase_handler.insert_data(payload)
        return "data processed !", 200
    except Exception as error:
        print("Erro no webhook")
        print(error)
        return "internal error", 500

