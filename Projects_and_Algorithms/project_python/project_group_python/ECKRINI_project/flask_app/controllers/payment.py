from flask_app import app
from flask import Flask,redirect,request, render_template
import stripe


stripe.api_key = "sk_test_51OMp4pDvNgAzLccg8LTuuUyfBShK3XNahrAi22LF0lVku2m1w8Sy5BJnEJdgRN7H4uv01lGdt2wmDbNxBxA4Ipv000iohlkt7N"
YOUR_DOMAIN = "http://localhost:5000/"

@app.route("/checkout")
def checkout():
    return render_template("checkout.html")
@app.route('/create-checkout-session', methods=['post'])
def create_checkout_session():
    try:

        checkout_session =stripe.checkout.Session.create(

            line_items = [
                {
                    'price' :'price_1OMpCQDvNgAzLccgmvT8IzgO',
                    'quantity': 1,
                }
            ],
            mode="subscription",
            success_url= YOUR_DOMAIN+"/sucsess.html",
            cancel_url= YOUR_DOMAIN+"/cancel.html",
        )

    except Exception as e:
        return str(e)
    return redirect(checkout_session.url, code=303)
