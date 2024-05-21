from flask_app import app
from flask import render_template , redirect , request ,session, flash
from flask_app.models.car import Car
from flask_app.models.user import User


#___________________________________________CREATE
@app.route('/new/car')
def new_car1() :
    if not "user_id" in session :
        return redirect("/")
    return render_template("add_car.html")



@app.route('/cars/create', methods=['post']) 
def create_car() :

    data={**request.form,"agency_id":int(session['user_id'])}
    Car.create(data)
    return redirect('/dashboard_agency')

#___________________________________________SHOW One


@app.route('/cars/<int:car_id>')

def one_car(car_id):
    if not 'user_id' in session:
        return redirect('/')
    one_car = Car.get_by_id({'id':car_id})
    return render_template("", car = one_car)

#___________________________________________SHOW Many Parties

@app.route('/my_cars')

def my_cars():
    if not 'user_id' in session:
        return redirect('/')
    user = User.get_by_email({'id':session['user_id']})
    cars = Car.get_user_parties({'user_id':session['user_id']})
    return render_template("my_parties.html", user = user , cars = cars)



#___________________________________________UPDATE

@app.route('/cars/<int:car_id>/edit')
def edit_car(car_id):
    if not 'user_id' in session:
        return redirect('/')
    my_car = Car.get_by_id({'id':car_id})
    print("🎈"*20, my_car)
    return render_template("edit_car.html", car = my_car)

@app.route('/cars/<int:car_id>/update', methods=['POST'])
def update_car(car_id):
    
    data = {
        **request.form,
        'id':car_id
    }
    Car.update(data)
    
    return redirect('/dashboard_agency')




#___________________________________________DELETE



@app.route('/rent/<int:id>/destroy', methods=['POST'])
def destroy(id):
    Car.destroy({'id':id,'user_id':session['user_id']})
    return redirect('/dashboard_client')

@app.route('/carsinag/<int:car_id>/destroy', methods=['POST'])
def destroy_two(car_id):
    Car.destroy_two({'id':car_id})
    return redirect('/dashboard_agency')


#* -------- Renting avaibility ------------

@app.route('/check_availability', methods=['POST'])
def check_availability():
    user_id =  session["user_id"]
    car_id=request.form.get('car_id')
    agency_id=request.form.get('agency_id')
    # Get car_id and rental period from the form data
    status = request.form.get('status')
    # car_id = request.form.get('car_id')
    start_time = request.form.get('start_time')
    end_time = request.form.get('end_time')

    # Check if the car is available for the requested period
    data_dict = {
        'user_id': user_id,
        'status': status,
        'car_id': car_id,
        'start_time': start_time,
        'end_time':end_time
    }
    is_available=  Car.is_car_rented_d(data_dict)
    if is_available:
        # Car is not available for rent
        
        flash("Car is not available !")
        return redirect(f'/booking/{car_id}/{agency_id}')

       
    else:
        
        Car.create_rented_car(data_dict)
        # Car available for rent during the requested period
        print("=========== is available")
        return redirect('/dashboard_client')