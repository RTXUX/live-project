<template>
    <div class="home">
        <div class="amap-wrapper">
            <div id="container"></div>
        </div>
    </div>
</template>

<script>
	/* eslint-disable */
    import AMap from "../utils/AMap";
    import axios from "axios"
    import consts from "@/assets/consts"
	export default {
		name: "Data3",
        data() {
		    return {
		    	resMap: null,
                map: null,
                lat: 26.08333,
                lng: 119.30000,
                data: null
            }
        },
        methods: {
			async initAMap() {
				try {
					// 修改
					this.resMap = await AMap();

					this.map = new this.resMap.Map("container", {
						resizeEnable: true, //是否监控地图容器尺寸变化
						zooms: [3, 19], //设置地图级别范围
						zoom: 14, //初始化地图层级
						zoomEnable: true, // 是否缩放
						scrollWheel: true, // 是否支持滚轮缩放
						dragEnable: true, // 是否支持鼠标拖拽平移
						jogEnable: true, // 是否支持缓动效果
						buildingAnimation: true, // 模块消失是否有动画效果
						center:  [this.lng, this.lat], //初始化地图中心点
                        viewMode: "3D"
					});
				} catch (err) {
					console.error(err);
				}
            },
            loadData() {
				axios.get(consts.apiBase + "data/3").then((response)=> {
					this.data = response.data
                    this.map.plugin(["AMap.Heatmap"], () => {
	                    let heatMap = new this.resMap.Heatmap(this.map, {
		                    radius: 25,
		                    opacity: [0, 0.8]
	                    })
	                    heatMap.setDataSet({
		                    data: this.data,
		                    max: this.data.length
	                    })
                    })

                })

            },
            drawHeatMap() {

            }
        },
        async mounted() {
			await this.initAMap()
            this.loadData()
        }
	}
</script>

<style scoped>
    .amap-wrapper #container {
        width: 100%;
        height: 800px;
    }
</style>