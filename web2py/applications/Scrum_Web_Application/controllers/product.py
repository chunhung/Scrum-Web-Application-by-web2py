# -*- coding: utf-8 -*-

#
# Product Controller
#
#

def index():
    """
    Shows all created products
    """
    products = db().select(db.product.id, db.product.title, orderby=db.product.id)
    return dict(products=products)

def create():
    form = crud.create(db.product, next=URL('index'))
    return dict(form=form)

def show():
    this_product = db.product(request.args(0)) or redirect(URL('index'))
    product_backlogs = db(db.backlog.product_id == this_product.id).select()
    return dict(product=this_product, backlogs=product_backlogs)

def edit():
    this_product = db.product(request.args(0)) or redirect(URL('index'))
    form = crud.update(db.product, this_product, next=URL('index'))
    return dict(form=form)
