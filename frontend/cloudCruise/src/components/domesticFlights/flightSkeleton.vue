<script setup lang="ts">
import { NSkeleton } from 'naive-ui'
</script>

<template>
  <article
    class="flex w-full gap-2 xs:gap-5 border-[#ddd] border-[1px] my-4 bg-white rounded-md h-[120px] px-4 py-2"
  >
    <aside class="flex w-[80%] flex-col gap-2">
      <div class="flex items-center w-full gap-2 xs:gap-5">
        <n-skeleton class="max-h-[50px] max-w-[50px] min-h-[50px] min-w-[50px]" circle>
        </n-skeleton>
        <n-skeleton class="h-[32px] w-[50%] xs:w-[40%] sm:w-[30%]" :sharp="false"> </n-skeleton>
      </div>
      <div class="flex w-full gap-2 xs:gap-5">
        <n-skeleton class="h-[45px] w-[45%]" :sharp="false"> </n-skeleton>

        <div class="flex w-[60%] gap-2 xs:gap-5">
          <n-skeleton class="w-1/3 h-full" :sharp="false"> </n-skeleton>
          <n-skeleton class="w-1/3 h-full" :sharp="false"> </n-skeleton>
          <n-skeleton class="w-1/3 h-full" :sharp="false"> </n-skeleton>
        </div>
      </div>
    </aside>
    <aside class="w-[20%]">
      <n-skeleton class="w-full h-full" :sharp="false"> </n-skeleton>
    </aside>
  </article>
</template>

<!-- <style scoped>
.flight-container {
  display: flex;
  border: 1px solid #dddddd;
  border-radius: 10px;
  align-items: center;
  width: 100%;
  height: 166px;
  margin-top: 10px;
  padding: 15px 10px;
  background-color: white;
}
.flight-details {
  display: flex;
  flex-direction: column;
  justify-content: center;
  flex-grow: 2;
  border-right: 5px solid #eee;
  /* margin-left: 1%; */
  /* background-color: #34c759; */
  height: 100%;
}
.flight-details-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-direction: row;
  flex-grow: 1;
  gap: 10px;
}
.flight-details-left {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  flex-direction: row;
}

.ariline-name {
  font-weight: 600;
  font-size: 20px;
}
.flight-no {
  font-size: 12px;
}
.airline-logo {
  object-fit: contain;
}
.refundable {
  color: #34c759;
  margin-right: 10px;
}

.flight-details-bottom {
  display: flex;
  justify-content: space-around;
  height: 100%;
}
img {
  object-fit: contain;
}
.bottom-details {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 4px;
}

.bottom-details p {
  color: gray;
}
.arrival-departure {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  height: 100%;
}
.plane-img {
  margin-top: 14px;
}

.time {
  font-size: 24px;
  font-weight: bold;
}
.sector {
  font-size: 16px;
  font-weight: 600;
}

.pricing-details {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin: 10px;
  /* gap: 40px; */
  height: 100%;
  align-items: center;
}
.prices {
  font-weight: 800;
}
.old-price {
  color: #ea2127;
}
.book-btn {
  background-color: #ea2127;
  color: white;
  font-weight: 700;
  /* margin-top: 45px; */
  outline: 0;
  padding: 10px;
  border: 0;
  border-radius: 5px;
  cursor: pointer;
  transition: 0.1s ease-in;
}
.book-btn:hover {
  background-color: #b80006;
}
.skeleton-naive {
  width: 100px;
  background-color: red;
}
.flight-details-left .skeleton-naive {
  width: 60px;
  height: 60px;
}
.skeleton-flightno {
  width: 275px;
}
.prices .skeleton-naive {
  width: 40px;
  height: 70px;
}
.departure .skeleton-naive,
.arrival .skeleton-naive,
.bottom-details .skeleton-naive {
  width: 120px;
  height: 30px;
}
.bottom-details .skeleton-naive {
  height: 20px;
}

@media only screen and (max-width: 1366px) {
  .flight-details-left .skeleton-naive {
    width: 40px;
    height: 38px;
  }
  .skeleton-flightno {
    width: 200px;
  }
  .prices .skeleton-naive {
    width: 100px;
    height: 40px;
  }
  .departure .skeleton-naive,
  .arrival .skeleton-naive,
  .bottom-details .skeleton-naive {
    width: 80px;
    height: 30px;
  }
  .bottom-details .skeleton-naive {
    height: 20px;
  }
}
@media only screen and (max-width: 1050px) {
  .flight-details-left .skeleton-naive {
    width: 40px;
    height: 38px;
  }
  .skeleton-flightno {
    width: 260px;
  }
  .prices .skeleton-naive {
    width: 100px;
    height: 40px;
  }
  .departure .skeleton-naive,
  .arrival .skeleton-naive,
  .bottom-details .skeleton-naive {
    width: 120px;
    height: 40px;
  }
  .bottom-details .skeleton-naive {
    height: 20px;
  }
}
@media only screen and (max-width: 936px) {
  .flight-details-left .skeleton-naive {
    width: 40px;
    height: 38px;
  }
  .skeleton-flightno {
    width: 250px;
  }
  .prices .skeleton-naive {
    width: 90px;
    height: 40px;
  }
  .departure .skeleton-naive,
  .arrival .skeleton-naive,
  .bottom-details .skeleton-naive {
    width: 100px;
    height: 40px;
  }
  .bottom-details .skeleton-naive {
    height: 20px;
  }
}
@media only screen and (max-width: 807px) {
  .flight-details-left .skeleton-naive {
    width: 40px;
    height: 38px;
  }
  .skeleton-flightno {
    width: 240px;
  }
  .prices .skeleton-naive {
    width: 80px;
    height: 40px;
  }
  .departure .skeleton-naive,
  .arrival .skeleton-naive,
  .bottom-details .skeleton-naive {
    width: 80px;
    height: 40px;
  }
  .bottom-details .skeleton-naive {
    height: 20px;
  }
}
@media only screen and (max-width: 700px) {
  .flight-details-left .skeleton-naive {
    width: 40px;
    height: 38px;
  }

  .prices .skeleton-naive {
    width: 80px;
    height: 40px;
  }
  .departure .skeleton-naive,
  .arrival .skeleton-naive,
  .bottom-details .skeleton-naive {
    width: 70px;
    height: 40px;
  }
  .bottom-details .skeleton-naive {
    height: 20px;
  }
}

@media only screen and (max-width: 560px) {
  .flight-details-left .skeleton-naive {
    width: 40px;
    height: 38px;
  }
  .skeleton-flightno {
    width: 100px;
  }
  .prices .skeleton-naive {
    width: 30px;
    height: 40px;
  }
  .departure .skeleton-naive,
  .arrival .skeleton-naive,
  .bottom-details .skeleton-naive {
    width: 50px;
    height: 40px;
  }
  .bottom-details .skeleton-naive {
    height: 20px;
  }
}
@media only screen and (max-width: 400px) {
  .flight-details-left .skeleton-naive {
    width: 40px;
    height: 38px;
  }
  .skeleton-flightno {
    width: 100px;
  }
  .prices .skeleton-naive {
    width: 30px;
    height: 40px;
    display: none;
  }
  .departure .skeleton-naive,
  .arrival .skeleton-naive,
  .bottom-details .skeleton-naive {
    width: 100px;
    height: 40px;
  }
  .bottom-details .skeleton-naive {
    height: 20px;
    display: none;
  }
}
</style> -->
