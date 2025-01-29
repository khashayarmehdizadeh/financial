from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Expense, Category

main = Blueprint('main', __name__)

@main.route('/')
def index():
    expenses = Expense.query.all()
    categories = Category.query.all()
    return render_template('index.html', expenses=expenses, categories=categories)

@main.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        title = request.form['title']
        amount = float(request.form['amount'])
        category_id = int(request.form['category'])

        new_expense = Expense(title=title, amount=amount, category_id=category_id)
        db.session.add(new_expense)
        db.session.commit()

        return redirect(url_for('main.index'))

    categories = Category.query.all()
    return render_template('add_expense.html', categories=categories)

@main.route('/delete_expense/<int:expense_id>')
def delete_expense(expense_id):
    expense = Expense.query.get(expense_id)
    if expense:
        db.session.delete(expense)
        db.session.commit()

    return redirect(url_for('main.index'))

@main.route('/add_category', methods=['POST'])
def add_category():
    name = request.form['name']
    new_category = Category(name=name)
    db.session.add(new_category)
    db.session.commit()

    return redirect(url_for('main.index'))
