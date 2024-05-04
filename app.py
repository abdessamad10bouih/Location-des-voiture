from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql
from voiture import Voiture
from manager import Manager
from client import Client
import sqlite3
import os 

# operation system


app = Flask(__name__)

app.secret_key = os.urandom(24)


# displaying only 3 cars
@app.route("/")
def display_cars():
    cars = fetch_cars_from_database()[:3]
    car_objects = []
    for car in cars:
        car_obj = Voiture(
            car[0], car[1], car[2], car[3], car[4], car[5], car[6], car[7]
        )
        car_objects.append(car_obj)
    return render_template("index.html", cars=car_objects)


def fetch_cars_from_database():
    conn = sql.connect("loc.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM voiture")
    cars = cursor.fetchall()
    conn.close()
    return cars

# displaying all cars
@app.route("/voitures")
def allcars():
    voitures = fetch_voitures_from_database()
    car_objects = []
    for voiture in voitures:
        car_obj = Voiture(
            voiture[0], voiture[1], voiture[2], voiture[3], voiture[4], voiture[5], voiture[6], voiture[7]
        )
        car_objects.append(car_obj)
    return render_template("detail.html", voitures=car_objects)


def fetch_voitures_from_database():
    conn = sql.connect("loc.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM voiture")
    voitures = cursor.fetchall()
    conn.close()
    return voitures


# deleting a car for admin
@app.route("/delete_car/<int:car_id>", methods=["POST"])
def delete_car(car_id):
    conn = sql.connect("loc.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM voiture WHERE id_voiture = ?", (car_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("all_cars_table"))

# deleting a car for manager

@app.route("/deleteVoiture/<int:car_id>", methods=["POST"])
def delete_car_manager(car_id):
    conn = sql.connect("loc.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM voiture WHERE id_voiture = ?", (car_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("all_cars_table_formanager"))


@app.route("/dashboard/voitures")
def all_cars_table_formanager():
    cars = fetch_cars_from_database()
    return render_template("/manager/voituresmana.html", cars=cars)


# //all cars table
@app.route("/dashboard/all_cars_table")
def all_cars_table():
    cars = fetch_cars_from_database()
    return render_template("cars.html", cars=cars)


def fetch_cars_from_database():
    conn = sql.connect("loc.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM voiture")
    cars = cursor.fetchall()
    conn.close()
    return cars

UPLOAD_FOLDER = "static/images/" 
ALLOWED_EXTENSIONS = {
    "png",
    "jpg",
    "jpeg",
}  # Specify the allowed file extensions

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def insert_car_into_database(
    marque, modele, immatriculation, categorie, prix, disponibilite, image_path
):
    conn = sqlite3.connect("loc.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO voiture (marque, modele, immatriculation, categorie, prix, disponibilite, image_url) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (marque, modele, immatriculation, categorie, prix, disponibilite, image_path),
    )
    conn.commit()
    conn.close()


@app.route("/car_detail/<int:car_id>")
def detailVoiture(car_id):
    car = find_car_by_id(car_id)
    if car:
        car_obj = Voiture(
            car[0], car[1], car[2], car[3], car[4], car[5], car[6], car[7]
        )
        return render_template("carDetaill.html", car=car_obj)
    else:
        return "Car not found", 404


def find_car_by_id(car_id):
    conn = sql.connect("loc.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM voiture WHERE id_voiture = ?", (car_id,))
    car = cursor.fetchone()
    conn.close()
    return car

# $_POST[""] = request.form
@app.route("/add_car", methods=["GET", "POST"])
def add_car():
    if request.method == "POST":
        marque = request.form["marque"]
        modele = request.form["modele"]
        immatriculation = request.form["immatriculation"]
        categorie = request.form["categorie"]
        prix = request.form["prix"]
        disponibilite = request.form["disponibilite"]
        file = request.files["image"]
        if file and allowed_file(file.filename):
            filename = file.filename
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(file_path)
            insert_car_into_database(
                marque,
                modele,
                immatriculation,
                categorie,
                prix,
                disponibilite,
                file_path,
            )
            return redirect(url_for("car_added"))
        else:
            flash("Invalid file type")
            return redirect(request.url)
    else:
        return render_template("add.html")


@app.route("/car_added")
def car_added():
    return redirect('add_car')


@app.route("/managers")
def display_managers():
    managers = fetch_managers_from_database()
    manaObj = []
    for manager in managers:
        mana = Manager(manager[0], manager[1], manager[2], manager[3], manager[4])
        manaObj.append(mana)
    return render_template("managers.html", managers=manaObj)


def fetch_managers_from_database():
    conn = sql.connect("loc.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM manager")
    mana = cursor.fetchall()
    conn.close()
    return mana


@app.route("/dashboard/clients")
def display_clients():
    clients = fetch_clients_from_database()
    ClientObj = []
    for client in clients:
        cli = Client(client[0], client[1], client[2], client[3], client[4])
        ClientObj.append(cli)
    return render_template("clients.html", clients=ClientObj)


@app.route("/lesclient")
def display_clients_formanager():
    clients = fetch_clients_from_database()
    ClientObj = []
    for client in clients:
        cli = Client(client[0], client[1], client[2], client[3], client[4])
        ClientObj.append(cli)
    return render_template("/manager/clientsmana.html", clients=ClientObj)


def fetch_clients_from_database():
    conn = sql.connect("loc.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM client")
    cli = cursor.fetchall()
    conn.close()
    return cli


def authenticate(username, password):
    conn = sqlite3.connect("loc.db")
    cursor = conn.cursor()
    query = "SELECT * FROM manager WHERE nom = ? AND mot_de_passe = ?"
    cursor.execute(query, (username, password))
    query_result = cursor.fetchone()
    conn.close()
    return query_result


def authenticateClient(username, password):
    conn = sqlite3.connect("loc.db")
    cursor = conn.cursor()
    query = "SELECT * FROM client WHERE email = ? AND telephone = ?"
    cursor.execute(query, (username, password))
    query_result = cursor.fetchone()
    conn.close()
    return query_result


def authenticateAdmin(username, password):
    conn = sqlite3.connect("loc.db")
    cursor = conn.cursor()
    query = "SELECT * FROM administrateur WHERE nom = ? AND mot_de_passe = ?"
    cursor.execute(query, (username, password))
    query_result = cursor.fetchone()
    conn.close()
    return query_result


@app.route("/registration", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        admin = authenticateAdmin(username, password)
        managers = authenticate(username, password)
        clients = authenticateClient(username, password)

        if admin:
            return render_template("dashboard.html", username=username, admin=admin)
        elif managers:
            return render_template("/manager/manaboard.html", username=username)
        elif clients:
            return render_template("index.html", username=username)
        else:
            error_message = "Invalid username or password"
            return render_template("login.html", error=error_message)
    else:
        return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
@app.route("/manger_dashboard")
def dashboardManager():
    return render_template("/manager/manaboard.html")

@app.route("/voitures")
def detail():
    username = request.args.get(
        "username"
    ) 
    return render_template("detail.html", username=username)


@app.route("/reserve_car/<int:car_id>", methods=["POST"])
def reserve_car(car_id):
    nom = request.form["nom"]
    prenom = request.form["prenom"]
    email = request.form["email"]
    telephone = request.form["telephone"]
    conn = sql.connect("loc.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO reservation (car_id, nom, prenom, email, telephone) VALUES (?, ?, ?, ?, ?)",
        (car_id, nom, prenom, email, telephone),
    )
    conn.commit()
    conn.close()

    flash(
        "Reservation request submitted successfully. A manager will review it shortly."
    )
    return redirect(url_for("detailVoiture", car_id=car_id))


@app.route("/manager/reservations")
def view_reservations():
    conn = sql.connect("loc.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservation WHERE status = 'Pending'")
    reservations = cursor.fetchall()
    conn.close()

    return render_template("manager/reservations.html", reservations=reservations)


@app.route("/manager/approve_reservation/<int:reservation_id>", methods=["POST"])
def approve_reservation(reservation_id):
    conn = sql.connect("loc.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE reservation SET status = 'Approved' WHERE reservation_id = ?",
        (reservation_id,),
    )
    conn.commit()
    conn.close()

    flash("Reservation approved.")
    return redirect(url_for("view_reservations"))


@app.route("/manager/reject_reservation/<int:reservation_id>", methods=["POST"])
def reject_reservation(reservation_id):
    conn = sql.connect("loc.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE reservation SET status = 'Rejected' WHERE reservation_id = ?",
        (reservation_id,),
    )
    conn.commit()
    conn.close()

    flash("Reservation rejected.")
    return redirect(url_for("view_reservations"))


@app.route(
    "/manager/update_reservation_status/<int:reservation_id>/<status>", methods=["POST"]
)
def update_reservation_status(reservation_id, status):
    conn = sql.connect("loc.db")
    cursor = conn.cursor()

    # Update the reservation status
    cursor.execute(
        "UPDATE reservation SET status = ? WHERE reservation_id = ?",
        (status, reservation_id),
    )
    conn.commit()
    conn.close()

    # Redirect back to the reservations page or to the previous page
    return redirect(url_for("view_reservations"))


@app.route("/")
def logout():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
