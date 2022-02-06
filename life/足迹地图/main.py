from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker

# 生成城市地图
c1 = (
    Map(init_opts=opts.InitOpts(width="1280px", height="720px"))
    .add(
        "我和桔桔的足迹",
         [
            # 直辖市
            ["北京", 23],
            # 河北
            ["秦皇岛", 24],
            # 广东
            ["深圳", 24],
        ],
        "china-cities",
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add(
        "我的足迹",
        [
            # 直辖市
            ["北京", 23], ["天津", 20], ["重庆", 23], ["上海", 19],
            # 山东
            ["潍坊", 23], ["日照", 23], ["济南", 17], ["青岛", 16], ["烟台", 10], ["威海", 12], ["泰安", 11], ["临沂", 8],
            # 河北
            ["秦皇岛", 24],
            # 内蒙古
            ["赤峰", 18],
            # 陕西
            ["西安", 11],
            # 山西
            ["大同", 22],
            # 辽宁
            ["大连", 12],
            # 江苏
            ["南京", 20], ["苏州", 13], ["扬州", 13], ["无锡", 13], ["南通", 13],
            # 浙江
            ["杭州", 22], ["嘉兴", 22],
            # 湖南
            ["长沙", 20], ["张家界", 20], ["湘西", 20],
            # 四川
            ["成都", 23],
            # 广东
            ["广州", 15], ["深圳", 24], ["珠海", 15],
        ],
        "china-cities",
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-中国地图（带城市）"),
        visualmap_opts=opts.VisualMapOpts(),
    )
    .render("C:\\Users\\11029\\Documents\\liyirui-git.github.io\\life\\足迹地图\\map_china_cities.html")
)

# 生成省份地图
c2 = (
    Map(init_opts=opts.InitOpts(width="1280px", height="720px"))
    .add(
        "我和桔桔的足迹",
        [
            # 直辖市
            ["北京", 23],
            # 其他省份
            ["广东", 24], ["河北", 24],
        ],
        "china",
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add(
        "我的足迹",
        [
            # 直辖市
            ["北京", 23], ["天津", 19], ["重庆", 23], ["上海", 19],
            # 其他省份
            ["山东", 23], ["内蒙古", 18], ["陕西", 11], ["山西", 22], ["辽宁", 12], ["江苏", 20], ["浙江", 22],["湖南", 20],
            ["四川", 23], ["广东", 24], ["河北", 24],
        ],
        "china",
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-中国地图"),
        visualmap_opts=opts.VisualMapOpts(),
    )
    .render("C:\\Users\\11029\\Documents\\liyirui-git.github.io\\life\\足迹地图\\map_china.html")
)
