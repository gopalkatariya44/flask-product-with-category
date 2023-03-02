import os

from werkzeug.utils import secure_filename

from base import app
from flask import render_template, request, redirect, jsonify, url_for

from base.com.dao.product_dao import ProductDAO
from base.com.dao.subcategory_dao import SubCategoryDAO
from base.com.vo.category_vo import CategoryVO
from base.com.dao.category_dao import CategoryDAO
from base.com.vo.product_vo import ProductVO
from base.com.vo.subcategory_vo import SubCategoryVO

product_folder = "base/static/product_images/"
app.config['PRODUCT_FOLDER'] = product_folder


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
@app.route("/admin/product/insert_product", methods=['post'])
def product_insert():
    product_category_id = request.form.get("categoryId")
    product_subcategory_id = request.form.get('subCategoryId')
    name = request.form.get('productName')
    desc = request.form.get('productDescription')
    product_price = request.form.get('productPrice')
    product_quantity = request.form.get('productQuantity')
    product_image = request.files.get('productImage')
    print(product_image)
    product_image_name = secure_filename(product_image.filename)
    print("Image Name: ", product_image_name)
    product_image_path = os.path.join(app.config['PRODUCT_FOLDER'])
    print(os.path.join(product_image_path, product_image_name))
    product_image.save(os.path.join(product_image_path, product_image_name))
    print(product_subcategory_id, name, desc)
    product_vo = ProductVO()
    product_dao = ProductDAO()
    product_vo.product_category_id = product_category_id
    product_vo.product_subcategory_id = product_subcategory_id
    product_vo.product_name = name
    product_vo.product_description = desc
    product_vo.product_price = product_price
    product_vo.product_quantity = product_quantity
    product_vo.product_image_name = product_image_name
    product_vo.product_image_path = product_image_path.replace("base",
                                                               "../..")
    product_dao = ProductDAO()
    product_dao.insert_product(product_vo)
    return redirect('/admin/product/view_product')


# @app.route('/admin/view_product')
# def admin_view_product():
#     dao = CategoryDAO()
#     view_list = dao.view_category()
#     # print("--->", list)
#     return render_template("../templates/category/view_category.html", list=view_list)
@app.route('/admin/product/view_product')
def product_view():
    product_dao = ProductDAO()
    product_vo_list_1 = product_dao.view_product()
    print("vo_list", product_vo_list_1)
    return render_template('product/view_product.html',
                           data=product_vo_list_1)


@app.route('/admin/product/delete_product')
def admin_delete_product():
    category_id = request.args.get('id')
    dao = ProductDAO()
    dao.delete_product(category_id)
    return redirect('/admin/product/view_product')
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
