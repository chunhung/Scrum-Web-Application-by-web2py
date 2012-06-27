# -*- coding: utf-8 -*-

#
# Backlog Controller
#
#

def index():
    """
    Shows all created backlogs of the product
    """
    this_product = db.product(request.args(0)) or redirect(URL('product', 'index'))
    backlogs = db(db.backlog.product_id == this_product.id).select()
    return dict(backlogs=backlogs)
                    
def create():
    this_product = db.product(request.args(0)) or redirect(URL('index'))
    db.backlog.product_id.default=this_product.id
    form = crud.create(db.backlog, next=URL('index'))
    return dict(form=form)
                            
def show():
    this_backlog = db.backlog(request.args(0)) or redirect(URL('index'))
    this_product = db.product(this_backlog.product_id)
    return dict(product=this_product, backlog=this_backlog)
                
def edit():
    this_backlog = db.backlog(request.args(0)) or redirect(URL('index'))
    this_product = db.product(this_backlog.product_id)
    form = crud.update(db.backlog, this_backlog, next=URL('index'))
    return dict(form=form)
