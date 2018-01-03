for rec in self:

  if rec.order_line:

    rec['x_first_product']=rec.order_line[0].product_id.display_name
