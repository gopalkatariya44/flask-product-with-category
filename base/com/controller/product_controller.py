from base import app
from flask import render_template, request, redirect, jsonify

from base.com.dao.subcategory_dao import SubCategoryDAO
from base.com.vo.category_vo import CategoryVO
from base.com.dao.category_dao import CategoryDAO
from base.com.vo.subcategory_vo import SubCategoryVO


@app.route('/admin/load_product')
def admin_load_product():
    category_dao = CategoryDAO()
    category_list = category_dao.view_category()
    return render_template('product/insert_product.html', list=category_list)


@app.route('/admin/product/load_subcategory')
def admin_load_product_subcategory():
    category_id = request.args.get('categoryId')
    print("--category_id-->", category_id)
    subcategory_vo = SubCategoryVO()
    subcategory_dao = SubCategoryDAO()
    subcategory_vo.subcategory_category_id = category_id
    category_list = subcategory_dao.view_ajax_subcategory_product(subcategory_vo)

    return jsonify([i.as_dict() for i in category_list])

#
# @app.route('/admin/insert_product', methods=['POST'])
# def admin_insert_product():
#     name = request.form.get('categoryName')
#     description = request.form.get('categoryDescription')
#
#     vo = CategoryVO()
#     dao = CategoryDAO()
#
#     vo.category_name = name
#     vo.category_description = description
#
#     dao.insert_category(vo)
#     return redirect('/admin/view_category')
#
#
# @app.route('/admin/view_product')
# def admin_view_product():
#     dao = CategoryDAO()
#     view_list = dao.view_category()
#     # print("--->", list)
#     return render_template("../templates/category/view_category.html", list=view_list)
#
#
# @app.route('/admin/delete_product/')
# def admin_delete_product():
#     category_id = request.args.get('id')
#     vo = CategoryVO()
#     dao = CategoryDAO()
#     vo.category_id = category_id
#     dao.delete_category(vo)
#     return redirect('/admin/view_category')
#
#
# @app.route('/admin/edit_product/')
# def admin_edit_product():
#     category_id = request.args.get('id')
#     vo = CategoryVO()
#     dao = CategoryDAO()
#     vo.category_id = category_id
#     edit_list = dao.edit_category(vo)
#     # print("-----", list[0]['category_name'])
#     return render_template('../templates/category/update_category.html', list=edit_list)
#
#
# @app.route('/admin/update_product/', methods=['POST'])
# def admin_update_product():
#     category_id = request.form.get('id')
#     name = request.form.get('categoryName')
#     description = request.form.get('categoryDescription')
#
#     vo = CategoryVO()
#     dao = CategoryDAO()
#
#     vo.category_id = category_id
#     vo.category_name = name
#     vo.category_description = description
#
#     dao.update_category(vo)
#     return redirect('/admin/view_category')
