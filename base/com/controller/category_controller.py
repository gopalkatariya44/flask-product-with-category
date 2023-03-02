from base import app
from flask import render_template, request, redirect
from base.com.vo.category_vo import CategoryVO
from base.com.dao.category_dao import CategoryDAO


@app.route('/')
@app.route('/admin/load_category')
def admin_load_category():
    return render_template('category/insert_category.html')


@app.route('/admin/insert_category', methods=['POST'])
def admin_insert_category():
    name = request.form.get('categoryName')
    description = request.form.get('categoryDescription')

    vo = CategoryVO()
    dao = CategoryDAO()

    vo.category_name = name
    vo.category_description = description

    dao.insert_category(vo)
    return redirect('/admin/view_category')


@app.route('/admin/view_category')
def admin_view_category():
    dao = CategoryDAO()
    view_list = dao.view_category()
    # print("--->", list)
    return render_template("category/view_category.html", list=view_list)


@app.route('/admin/delete_category/')
def admin_delete_category():
    category_id = request.args.get('id')
    vo = CategoryVO()
    dao = CategoryDAO()
    vo.category_id = category_id
    dao.delete_category(vo)
    return redirect('/admin/view_category')


@app.route('/admin/edit_category/')
def admin_edit_category():
    category_id = request.args.get('id')
    vo = CategoryVO()
    dao = CategoryDAO()
    vo.category_id = category_id
    edit_list = dao.edit_category(vo)
    # print("-----", list[0]['category_name'])
    return render_template('category/update_category.html', list=edit_list)


@app.route('/admin/update_category/', methods=['POST'])
def admin_update_category():
    category_id = request.form.get('id')
    name = request.form.get('categoryName')
    description = request.form.get('categoryDescription')

    vo = CategoryVO()
    dao = CategoryDAO()

    vo.category_id = category_id
    vo.category_name = name
    vo.category_description = description

    dao.update_category(vo)
    return redirect('/admin/view_category')
