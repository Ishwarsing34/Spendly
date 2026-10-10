from flask import Flask, render_template, session, redirect, url_for, request
from database.db import init_db, get_db
import sqlite3

app = Flask(__name__)
app.secret_key = 'spendly_secret_key'

# Initialize database on startup
with app.app_context():
    init_db()


# ------------------------------------------------------------------ #
# Routes                                                              #
# ------------------------------------------------------------------ #

@app.route("/")
def landing():
    return render_template("landing.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        db = get_db()
        try:
            db.execute(
                "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                (name, email, password)
            )
            db.commit()
            # Log the user in immediately after registration
            user = db.execute("SELECT id FROM users WHERE email = ?", (email,)).fetchone()
            session['user_id'] = user['id']
            return redirect(url_for('profile'))
        except sqlite3.IntegrityError:
            return render_template("register.html", error="Email or username already exists")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        db = get_db()
        user = db.execute(
            "SELECT * FROM users WHERE email = ? AND password = ?",
            (email, password)
        ).fetchone()

        if user:
            session['user_id'] = user['id']
            return redirect(url_for('profile'))
        else:
            return render_template("login.html", error="Invalid email or password")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('landing'))


@app.route("/profile")
def profile():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    db = get_db()
    user = db.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()

    if not user:
        return redirect(url_for('login'))

    expenses = db.execute(
        "SELECT * FROM expenses WHERE user_id = ? ORDER BY date DESC",
        (user_id,)
    ).fetchall()

    total = sum(exp['amount'] for exp in expenses)

    return render_template("profile.html", user=user, expenses=expenses, total=total)


@app.route("/terms")
def terms():
    return render_template("terms.html")


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


# ------------------------------------------------------------------ #
# Expense Management                                                  #
# ------------------------------------------------------------------ #

@app.route("/expenses/add", methods=["GET", "POST"])
def add_expense():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    if request.method == "POST":
        amount = request.form.get("amount")
        category = request.form.get("category")
        description = request.form.get("description")
        date = request.form.get("date")

        db = get_db()
        db.execute(
            "INSERT INTO expenses (user_id, amount, category, description, date) VALUES (?, ?, ?, ?, ?)",
            (user_id, amount, category, description, date)
        )
        db.commit()
        return redirect(url_for('profile'))

    return render_template("add_expense.html")


@app.route("/expenses/<int:id>/edit", methods=["GET", "POST"])
def edit_expense(id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    db = get_db()
    expense = db.execute("SELECT * FROM expenses WHERE id = ? AND user_id = ?", (id, user_id)).fetchone()

    if not expense:
        return "Expense not found", 404

    if request.method == "POST":
        amount = request.form.get("amount")
        category = request.form.get("category")
        description = request.form.get("description")
        date = request.form.get("date")

        db.execute(
            "UPDATE expenses SET amount = ?, category = ?, description = ?, date = ? WHERE id = ?",
            (amount, category, description, date, id)
        )
        db.commit()
        return redirect(url_for('profile'))

    return render_template("edit_expense.html", expense=expense)


@app.route("/expenses/<int:id>/delete", methods=["POST"])
def delete_expense(id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    db = get_db()
    db.execute("DELETE FROM expenses WHERE id = ? AND user_id = ?", (id, user_id))
    db.commit()
    return redirect(url_for('profile'))


if __name__ == "__main__":
    app.run(debug=True, port=5001)
