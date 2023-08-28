from domain_admin.model.image_model import ImageModel

# 保存图片
def saveImage(image_url,description):
    row = ImageModel.create(
        image_url = image_url,
        description = description,
        status = 0
    )
    return row

# 获取所有的图片
def get_all_image():
    list=[]
    query = ImageModel.select()
    # 遍历记录并处理每一条记录
    for record in query:
        list.append(record)
    return list