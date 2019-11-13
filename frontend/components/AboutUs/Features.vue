<template>
  <section>
    
    <!-- FEATURE 1 -->
    <div class="Title">주요 기능 1: 전체보기 vs 상세보기</div>
    <div class="Content">
      <p class="txt1">전체보기: 출퇴근 시간과 연봉을 한눈에 파악해요~</p>
      <div class="imgBox">
        <img class="overviewImg" src="https://i.imgur.com/pIHqf7i.png" alt="">
      </div>
      <br>
      <p class="txt2">지도에 표시된 마커 모양과 색상으로 대략적인 연봉 및 출퇴근 시간 수준을 알 수 있습니다.</p>
      <div class="markerDesc">
        <div class="markerRow">
          <div class="marker">
            <img src="https://i.imgur.com/9EMDLEC.png" alt="">
            <p class="label">30분 이내</p>
          </div>
          <div class="marker">
            <img src="https://i.imgur.com/zEAWAej.png" alt="">
            <p class="label">45분 이내</p>
          </div>
          <div class="marker">
            <img src="https://i.imgur.com/YrEPYUO.png" alt="">
            <p class="label">60분 이내</p>
          </div>
          <div class="marker">
            <img src="https://i.imgur.com/8gUciAP.png" alt="">
            <p class="label">60분 초과</p>
          </div>
        </div>
        <div class="markerRow">
          <div class="marker">
            <img src="https://i.imgur.com/8gUciAP.png" alt="">
            <p class="label">연봉 4000 미만</p>
          </div>
          <div class="marker">
            <img src="https://i.imgur.com/MGIH1Pi.png" alt="">
            <p class="label">연봉 4000 이상</p>
          </div>
          <div class="marker">
            <img src="https://i.imgur.com/UNqHYfQ.png" alt="">
            <p class="label">연봉 5000 이상</p>
          </div>
        </div>
        <div class="markerRow">
          <div class="marker">
            <img src="https://i.imgur.com/5VcItZX.png" alt="">
            <p class="label">현재 채용 중인 공고 없음</p>
          </div>
        </div>
      </div>
      <br>
      <br>
      <br>
      <p class="txt1">상세보기: 회사의 상세 정보까지 확인해요~</p>
      <p class="txt2">관심 있는 회사의 마커를 클릭하면 좌측에 회사 상세 정보가 뜹니다.</p>
      <div class="imgBox">
        <img class="detailImg" src="https://i.imgur.com/tkM85n9.png" alt="">
      </div>
    </div>

    <div class="divider"></div>

    <!-- FEATURE 2 -->
    <div class="Title">주요 기능 2: 나만의 조건 검색</div>
    <div class="Content">
      <p class="txt1">출발 지하철역을 설정해요~</p>
      <p class="txt2">임의로 지정한 지하철역으로부터의 출퇴근 거리를 확인할 수 있습니다.</p>
      <div class="imgBox">
        <img class="departureImg" src="https://i.imgur.com/Dfkv5i9.png" alt="">
      </div>
      <br>
      <p class="txt1">연봉, 출퇴근시간, 기업 규모로 필터링해요~</p>
      <div class="imgBox">
        <img class="filterImg" src="https://i.imgur.com/NjWptet.png" alt="">
      </div>
    </div>

    <div class="divider"></div>

    <!-- FEATURE 3 -->
    <div class="Title">주요 기능 3: 지도 탐방</div>
    <div class="Content">
      <p class="txt1">지도를 드래그하면 주변의 회사 목록이 좌측에 실시간으로 업데이트됩니다.</p>
      <div class="imgBox">
        <img class="navImg" src="https://i.imgur.com/aypSA7g.png" alt="">
      </div>
      <br>
      <p class="txt1">검색창에서 특정 회사를 찾아볼 수도 있어요~</p>
      <div class="imgBox">
        <img src="https://i.imgur.com/iQ3vEO4.png" alt="" class="searchImg">
      </div>
    </div>

  </section>
</template>

<script>
export default {
  name: "Features"
}
</script>

<style lang="scss" scoped>
@import '~/assets/aboutus.scss';

.divider {
  width: 100%;
  height: 20px;
  margin: 40px auto;
  transform: skew(-30deg);
  background: rgba(88, 180, 230, 0.5);
  box-shadow: inset 0 0 10px 0px rgb(74, 165, 215), 0 0 2px 0 rgb(74, 165, 215);
}

// FEATURE 1
.overviewImg {
  height: 200px;
}
.detailImg {
  height: 300px;
}
.markerDesc {
  max-width: 600px;
}
.markerRow {
  display: flex;
  justify-content: space-evenly;
  padding: 10px 0;
  border-bottom: 1px solid #CCC;
  &:last-child {
    border: none;
  }
  .marker {
    img {
      width: 80px;
      display: inline-block;
    }
    .label {
      font-size: 14px;
    }
  }
}



// FEATURE 2
.departureImg {
  height: 200px;
}
.filterImg {
  height: 150px;
}

// FEATURE 3
.navImg {
  height: 200px;
}
.searchImg {
  height: 150px;
}

</style>