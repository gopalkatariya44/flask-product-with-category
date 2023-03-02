from base import app
from flask import render_template, request, redirect
from base.com.vo.subcategory_vo import SubCategoryVO
from base.com.dao.category_dao import CategoryDAO
from base.com.dao.subcategory_dao import SubCategoryDAO


@app.route('/admin/load_subcategory')
def admin_load_subcategory():
    category_dao = CategoryDAO()
    category_list = category_dao.view_category()
    return render_template('subcategory/insert_subcategory.html', list=category_list)


@app.route('/admin/insert_subcategory', methods=['POST'])
def admin_insert_subcategory():
    category_id = request.form.get('categoryId')
    name = request.form.get('subCategoryName')
    description = request.form.get('subCategoryDescription')

    subcategory_vo = SubCategoryVO()
    subcategory_dao = SubCategoryDAO()

    subcategory_vo.subcategory_name = name
    subcategory_vo.subcategory_description = description
    subcategory_vo.subcategory_category_id = category_id

    subcategory_dao.insert_subcategory(subcategory_vo)
    return redirect('/admin/view_subcategory')


@app.route('/admin/view_subcategory')
def admin_view_subcategory():
    dao = SubCategoryDAO()
    view_list = dao.view_subcategory()
    print("--->", view_list)
    return render_template("subcategory/view_subcategory.html", list=view_list)


@app.route('/admin/delete_subcategory/')
def admin_delete_subcategory():
    subcategory_id = request.args.get('id')
    subcategory_dao = SubCategoryDAO()
    subcategory_dao.delete_subcategory(subcategory_id)
    return redirect('/admin/view_subcategory')


@app.route('/admin/edit_subcategory/')
def admin_edit_subcategory():
    dao = CategoryDAO()
    category_list = dao.view_category()

    subcategory_id = request.args.get('id')
    subcategory_vo = SubCategoryVO()
    subcategory_dao = SubCategoryDAO()
    subcategory_vo.subcategory_id = subcategory_id
    edit_list = subcategory_dao.edit_subcategory(subcategory_vo)
    # print("-----", list[0]['category_name'])
    return render_template('subcategory/update_subcategory.html', list=edit_list, category_list=category_list)


@app.route('/admin/update_subcategory/', methods=['POST'])
def admin_update_subcategory():
    subcategory_id = request.form.get('id')
    name = request.form.get('subCategoryName')
    description = request.form.get('subCategoryDescription')
    category_id = request.form.get('categoryId')
    subcategory_vo = SubCategoryVO()
    subcategory_dao = SubCategoryDAO()

    subcategory_vo.subcategory_id = subcategory_id
    subcategory_vo.subcategory_name = name
    subcategory_vo.subcategory_description = description
    subcategory_vo.subcategory_category_id = category_id

    subcategory_dao.update_subcategory(subcategory_vo)
    return redirect('/admin/view_subcategory')
