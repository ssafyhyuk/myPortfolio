<template>
  <div>
    <KakaoMap :lat="37.501291" :lng="127.039602" :draggable="true" :level="2" @onLoadKakaoMap="onLoadKakaoMap">
      <KakaoMapMarker
        v-for="(marker, index) in markerList"
        :key="marker.key === undefined ? index : marker.key"
        :lat="marker.lat"
        :lng="marker.lng"
        :infoWindow="marker.infoWindow"
        :clickable="true"
        @onClickKakaoMapMarker="onClickMapMarker(marker)"
      />
    </KakaoMap>
  </div>
</template>

<script setup lang="ts">
  import { ref, watch } from 'vue'
  import { KakaoMap, KakaoMapMarker, type KakaoMapMarkerListItem } from 'vue3-kakao-maps'

  const props = defineProps({
    findName: String,
  })

  const map = ref<kakao.maps.Map>()
  const markerList = ref<KakaoMapMarkerListItem[]>([])

  const onLoadKakaoMap = (mapRef: kakao.maps.Map) => {
    map.value = mapRef
  }

  const onClickMapMarker = (markerItem: KakaoMapMarkerListItem): void => {
    if (markerItem.infoWindow?.visible !== null && markerItem.infoWindow?.visible !== undefined) {
      markerItem.infoWindow.visible = !markerItem.infoWindow.visible;
    } else {
      markerItem.infoWindow.visible = true;
    }
  }

  // Watch for changes in findName prop
  watch(() => props.findName, (newValue, oldValue) => {
    // Call a function to update the map when findName changes
    updateMap(newValue)
  })

  const updateMap = (findName: string) => {
    // Clear existing markers
    markerList.value = []

    // Perform any map update logic here based on the findName value
    // For example, perform a new search using findName and update markers accordingly
    const ps = new kakao.maps.services.Places()
    ps.keywordSearch(findName, placesSearchCB)
  }

  const placesSearchCB = (data: kakao.maps.services.PlacesSearchResult, status:kakao.maps.services.Status): void => {
    if (status === kakao.maps.services.Status.OK) {
      const bounds = new kakao.maps.LatLngBounds()

      for (let marker of data) {
        const markerItem: KakaoMapMarkerListItem = {
          lat: marker.y,
          lng: marker.x,
          infoWindow: {
            content: marker.place_name,
            visible: false
          }
        }
        markerList.value.push(markerItem)
        bounds.extend(new kakao.maps.LatLng(Number(marker.y), Number(marker.x)))
      }

      map.value?.setBounds(bounds)
    }
  }
</script>

<style scoped>

</style>
