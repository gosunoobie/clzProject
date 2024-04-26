<template>
  <div class="[w-100vw] overflow-x-hidden mt-0 md:mt-[100px]">
    <!-- <section
      class="flex gap-2 xl:gap-6 mx-auto w-full md:w-[90%] lg:w-auto flex-col-reverse md:flex-row md:mx-[40px] xl:mx-[100px] 2xl:mx-[7.5%] mb-4"
    >
      <article class="">
        <aside
          class="text-center md:text-start max-w-auto md:max-w-[460px] lg:max-w-[550px] xl:max-w-[600px] 2xl:max-w-[800px]"
        >
          <h1
            class="text-2xl xs:text-[30px] xsm:text-[48px] mx-auto w-[310px] xs:w-[400px] xsm:w-[500px] md:w-auto lg:text-[66px] xl:text-[72px] 2xl:text-[80px] font-secular font-medium leading-normal"
          >
            Ready to Explore The Beauty of Wonderful Nepal
          </h1>

          <p
            class="mx-auto w-[90%] md:w-auto text-[#ACA7A7] font-['Poppins'] text-sm xsm:text-base lg:text-lg xl:text-xl 2xl:text-2xl leading-normal my-5 md:my-10"
          >
            <span class="text-black">Trip</span><span class="text-primary-400">Turbo</span>
            is Nepal's largest online travel platform with the widest range of travel products and
            services by hundreds of verified vendors all across Nepal.
          </p>
          <div class="flex justify-center gap-5 lg:gap-8 md:justify-start">
            <a
              target="_blank"
              ><img
                loading="lazy"
                src="../assets/layout/image/googlestore.webp"
                alt="googlestore.webp"
                class="h-[36px] xs:h-[45px] lg:h-[60px] 2xl:h-[70px] hover:scale-105 transition-all"
            /></a>
            <a
              ><img
                loading="lazy"
                src="../assets/layout/image/appstore.webp"
                alt="appStoreImage.webp"
                class="h-[36px] xs:h-[45px] lg:h-[60px] 2xl:h-[70px] hover:scale-105 transition-all"
            /></a>
          </div>
        </aside>
      </article>

      <article
        class="w-full max-w-full min-w-full md:max-w-[50%] md:min-w-[50%] grid justify-center"
      >
        <aside
          class="relative w-[175px] xsm:w-[245px] lg:w-[315px] xl:w-[350px] h-[250px] xsm:h-[350px] lg:h-[450px] xl:h-[500px] mt-[75px] xs:mt-[80px] md:mt-[90px] group"
        >
          <img
            loading="lazy"
            src="../assets/layout/image/plane_taking_off.gif"
            alt="planeImage.gif"
            class="absolute w-[45px] xsm:w-[60px] xl:w-[70px] left-[-20%] xs:left-[-17.5%] lg:left-[-12.5%] top-[4cqh] md:top-[6cqh] translate-x-[-50%] translate-y-[-50%]"
          />
          <img
            loading="lazy"
            src="../assets/layout/image/boating_in_lake.gif"
            alt="boatingImage.gif"
            class="absolute w-[45px] xsm:w-[60px] xl:w-[70px] left-[10%] xs:left-[15%] lg:left-[20%] top-[-4cqh] md:top-[-6cqh] translate-x-[-50%] translate-y-[-50%]"
          />
          <img
            loading="lazy"
            src="../assets/layout/image/hotel_display.gif"
            alt="hotel.gif"
            class="absolute w-[45px] xsm:w-[60px] xl:w-[70px] left-[50%] xs:left-[60%] top-[-5cqh] md:top-[-7cqh] translate-x-[-50%] translate-y-[-50%]"
          />
          <img
            loading="lazy"
            src="../assets/layout/image/paragliding_updown.gif"
            alt="pararglidng.gif"
            class="absolute w-[45px] xsm:w-[60px] xl:w-[70px] right-[-15%] xs:right-[-25%] lg:right-[-15%] top-[-2.5cqh] lg:top-[-5cqh] translate-x-[-50%] translate-y-[-50%]"
          />

          <img
            loading="lazy"
            src="../assets/layout/image/luggage_dropping.gif"
            alt="luggage.gif"
            class="absolute w-[45px] xsm:w-[60px] xl:w-[70px] left-[120%] xs:left-[127.5%] top-[4cqh] lg:top-[7cqh] translate-x-[-50%] translate-y-[-50%]"
          />

          <img
            loading="lazy"
            src="../assets/layout/image/phoneFront.webp"
            class="absolute top-[1.5%] left-[-7.5%] xs:left-[0cqw] h-[250px] xsm:h-[350px] lg:h-[450px] xl:h-[500px] z-10 rotate-0 transition-all ease-in-out duration-500 group-hover:rotate-[-12deg] lg:group-hover:rotate-[-15deg] cursor-pointer group-hover:scale-105"
            alt="frontPhoneImage.webp"
          />
          <img
            loading="lazy"
            src="../assets/layout/image/phoneBack.webp"
            class="absolute left-[16%] xs:left-[22%] top-[-3%] h-[250px] xsm:h-[350px] lg:h-[450px] xl:h-[500px] z-[9] rotate-0 transition-all ease-in-out cursor-pointer duration-500 group-hover:rotate-[10deg] lg:group-hover:rotate-[15deg] group-hover:scale-105"
            alt="phoneBackImage.webp"
          />
        </aside>
      </article>
    </section> -->

    <section
      class="flex flex-col md:flex-row justify-between w-full md:w-[87.5%] lg:w-[85%] xl:w-[80%] pt-[20px] lg:pt-[50px] xl:pt-[80px] mb-0 xl:mb-10 mx-auto group"
    >
      <article class="grid items-center justify-center md:justify-start pl-0 2xl:pl-[2%]">
        <aside
          class="relative w-[280px] xs:w-[325px] xsm:w-[400px] md:min-w-[380px] lg:min-w-[475px] max-w-[600px] xl:w-[600px] h-[320px] xsm:h-[400px] md:h-[495px] cursor-pointer"
        >
          <img
            loading="lazy"
            :src="ladderman"
            alt="ladderman image"
            class="absolute w-[100cqw] top-[50%] left-[50%] translate-x-[-50%] translate-y-[-50%] group-hover:top-[46%] z-10 transition-all duration-1000 ease-in-out"
          />
          <img
            loading="lazy"
            :src="sun"
            alt="sun image"
            class="absolute w-[10cqw] xs:w-[8cqw] md:w-[6cqw] rotate-0 top-8 group-hover:top-0 left-[5%] z-8 transition-all duration-[1250ms] ease-in-out group-hover:rotate-[180deg] group-hover:scale-125"
          />
          <img
            loading="lazy"
            :src="cloud1"
            alt="cloud1 image"
            class="absolute w-[15cqw] xs:w-[12.5cqw] md:w-[10cqw] top-[15%] group-hover:top-[30%] left-[58%] z-9 transition-all duration-1000 ease-in-out"
          />
          <img
            loading="lazy"
            :src="cloud2"
            alt="cloud2 image"
            class="absolute w-[10cqw] xs:w-[8cqw] md:w-[6.5cqw] top-[42%] left-[55%] z-9 group-hover:scale-125 group-hover:top-5 transition-all duration-1000 ease-in-out"
          />
          <img
            loading="lazy"
            :src="cloud3"
            alt="cloud3 image"
            class="absolute w-[30cqw] xs:w-[25cqw] md:w-[20cqw] top-[40%] group-hover:scale-90 group-hover:top-[30%] left-0 z-9 cursor-pointer transition-all duration-1000 ease-in-out"
          />
          <img
            loading="lazy"
            :src="cloud4"
            alt="cloud4 image"
            class="absolute w-[12cqw] xs:w-[10cqw] md:w-[8cqw] top-[10%] left-[18%] z-9 group-hover:left-[1%] transition-all duration-1000 ease-in-out"
          />
        </aside>
      </article>
      <article class="w-auto md:w-fit 2xl:w-[40%]">
        <aside
          class="w-[65%] text-center md:text-start mx-auto md:mx-0 md:w-full lg:w-[470px] xl:w-[520px] 2xl:w-[full%] mt-0 md:mt-[80px] lg:mt-[30px]"
        >
          <h3
            data-aos="fade-left"
            class="text-primary-400 font-secular font-normal text-[26px] xs:text-[30px] xsm:text-[40px] lg:text-[50px] xl:text-[60px]"
          >
            Our Vision
          </h3>
          <h2
            data-aos="fade-left"
            class="text-black font-normal text-[30px] xs:text-[36px] xsm:text-[60px] lg:text-[75px] xl:text-[90px] font-[''Roboto] leading-[1.15] my-4 xs:mb-5"
          >
            Making Flight Simple
          </h2>
          <p
            data-aos="fade-left"
            class="font-['Poppins'] text-sm xs:text-[18px] lg:text-[24px] xl:text-[30px] font-normal"
          >
            <span class="font-bold leading-normal text-primary-400"> Skybound Excellence, </span>
            Grounded in Service
          </p>
        </aside>
      </article>
    </section>

    <section
      class="relative w-full h-[140px] md:h-[170px] lg:h-[200px] xl:h-[230px] overflow-x-hidden z-9"
    >
      <aside class="absolute bottom-0 z-10 w-full h-5 bg-white"></aside>
      <article class="flex justify-start animate-marquee">
        <aside
          class="min-w-full h-[140px] md:h-[170px] lg:h-[200px] bg-no-repeat xl:h-[230px] bg-cover bg-center"
          :style="`background-image:url('${banner}')`"
        ></aside>
        <aside
          class="min-w-full h-[140px] md:h-[170px] lg:h-[200px] bg-no-repeat xl:h-[230px] bg-cover bg-center"
          :style="`background-image:url('${banner}')`"
        ></aside>
      </article>
    </section>
    <section
      class="flex my-0 xl:my-20 mx-auto flex-col-reverse md:flex-row justify-between w-full md:w-[87.5%] lg:w-[85%] 2xl:w-[80%] group"
    >
      <article class="w-[75%] text-center md:text-start mx-auto md:w-[50%]">
        <aside class="w-full lg:w-[90%]">
          <h3
            data-aos="fade-right"
            class="text-primary-400 font-secular font-normal text-[26px] xs:text-[30px] xsm:text-[40px] lg:text-[50px] xl:text-[60px] mt-0 mb-4 xl:mt-12 xl:mb-8"
          >
            Our Mission
          </h3>
          <p
            data-aos="fade-right"
            class="text-[14px] xs:text-[18px] md:text-[22px] lg:text-[24px] xl:text-[32px] font-['Poppins'] font-medium"
          >
            To create a culture where all stakeholders are empowered with choice and control by
            building a responsible travel ecosystem that uses technology & processes to deliver
            exceptional service & support with simplicity at its core.
          </p>
        </aside>
      </article>
      <article class="grid items-center justify-center">
        <aside
          class="relative max-w-[280px] xs:max-w-[325px] xsm:max-w-[375px] lg:max-w-[475px] xl:min-w-[575px] mt-12 mb-8 md:my-0"
        >
          <img
            loading="lazy"
            :src="missionBackground"
            alt="mission background image"
            class="w-[100cqw]"
          />

          <img
            loading="lazy"
            :src="cubeImage"
            alt="cube image "
            class="w-[60%] absolute left-[0%] top-[19%] scale-1 group-hover:top-[12%] transition-all duration-700 ease-in-out"
          />

          <img
            loading="lazy"
            :src="smallGear"
            alt="small gear image"
            class="w-[5%] absolute left-[20%] top-[30%] scale-1 group-hover:top-[23%] rotate-0 group-hover:rotate-180 transition-all duration-1000 ease-in-out"
          />
          <img
            loading="lazy"
            :src="bigGear"
            alt="big gear image"
            class="w-[7.75%] absolute left-[22.5%] top-[22.25%] scale-1 group-hover:top-[15.5%] rotate-0 group-hover:rotate-[-180deg] transition-all duration-1000 ease-in-out"
          />
          <img
            loading="lazy"
            :src="bigStar"
            alt="big star image"
            class="w-[7.75%] absolute left-[5.5%] top-[51%] scale-1 group-hover:top-[44%] rotate-0 transition-all duration-1000 ease-in-out z-[12]"
          />
          <img
            loading="lazy"
            :src="smallStar"
            alt="small star image"
            class="w-[5.5%] absolute left-[4%] top-[52%] scale-1 group-hover:top-[44.5%] rotate-0 transition-all duration-1000 ease-in-out z-[11] group-hover:left-[2.9%]"
          />
          <img
            loading="lazy"
            :src="smallStar"
            alt="small star image"
            class="w-[5.5%] absolute left-[9%] top-[52%] scale-1 group-hover:top-[44.5%] rotate-0 transition-all duration-1000 ease-in-out z-[11] group-hover:left-[10.1%]"
          />
          <img
            loading="lazy"
            :src="clock"
            alt="clock image"
            class="w-[10%] absolute left-[45.5%] top-[25%] scale-1 group-hover:top-[18%] rotate-0 transition-all duration-1000 ease-in-out z-[11]"
          />
          <img
            loading="lazy"
            :src="clockHandLeft"
            alt="clock hand left image"
            class="w-[2%] absolute left-[50.3%] top-[27.5%] scale-1 group-hover:top-[22.5%] rotate-0 group-hover:rotate-90 group-hover:left-[50.75%] transition-all duration-1000 ease-in-out z-[12]"
          />
          <img
            loading="lazy"
            :src="bar"
            alt="bar image"
            class="w-[7%] h-[6%] group-hover:h-[8%] absolute left-[15.5%] top-[81.5%] scale-1 group-hover:top-[72.5%] rotate-0 transition-all duration-700 ease-in-out z-[12]"
          />
          <img
            loading="lazy"
            :src="verify"
            alt="verify image"
            class="w-[5%] absolute left-[51%] top-[24.5%] scale-1 group-hover:top-[18%] rotate-0 transition-all duration-1000 ease-in-out z-[12]"
          />
          <!-- <div class="circle absoulte border-[1px] border-primary-400"></div> -->
        </aside>
      </article>
    </section>
  </div>
</template>

<script lang="ts" setup>
import banner from '../assets/layout/image/banner.webp'
import ladderman from '../assets/layout/image/ladderman/ladderman.webp'
import sun from '../assets/layout/image/ladderman/sun.png'
import cloud1 from '../assets/layout/image/ladderman/cloud1.png'
import cloud2 from '../assets/layout/image/ladderman/cloud2.png'
import cloud3 from '../assets/layout/image/ladderman/cloud3.png'
import cloud4 from '../assets/layout/image/ladderman/cloud4.png'
import missionBackground from '../assets/layout/image/mission/background.webp'
import cubeImage from '../assets/layout/image/mission/boxContainer.png'
import smallGear from '../assets/layout/image/mission/smallGear.png'
import bigGear from '../assets/layout/image/mission/bigGear.png'
import smallStar from '../assets/layout/image/mission/smallStar.png'
import bigStar from '../assets/layout/image/mission/bigStar.png'
import clock from '../assets/layout/image/mission/clock.png'
import clockHandLeft from '../assets/layout/image/mission/clockhand.png'
import bar from '../assets/layout/image/mission/bar.png'
import verify from '../assets/layout/image/mission/verify.png'
</script>

<style scoped>
.font-secular {
  font-family: 'Secular One';
}
</style>
