export interface ServiceListType {
  id: number
  name: string
  detail: string
  thumbnail: string
  hasDifferentType: boolean
  serviceTypes: ServiceCategoryType[]
}

export interface ServiceCategoryType {
  id: number
  name: string
  thumbnail: string
}

export interface ActivityResultType {
  images: any[]
  data: ActivityListType[]
}

export interface ActivityListType {
  id: number
  averageRating: number
  totalReviews: number
  startingPrice: number
  name: string
  detail: string
  district: string
  serviceName: string[]
  sServiceName: string
  thumbnail: string
  schedule: string
}

export interface ActivityPricingType {
  id: number
  serviceType: string
  image: string
  displayName: string
  totalPriceAfterDiscount: number
  category: string
  timeUnit: string
  nationality: string
  ageGroup: 'Adult' | 'Child'
  isBulkPrice: boolean
  isStudent: boolean
  nprPrice: number
  usdPrice: number
  rewardCoin: string
  commission: number
  discount: number
  ofProviderServiceType: number
  ofInventory: number
  val?: number
}
export interface InventoryType {
  id: number
  serviceType: number
  inventoryId: number
  serviceTypeId: number
  serviceTypeName: string
  businessServiceType: number
  serviceName: string
  displayName: string
  categoryPhoto: string
  ticketInfo: string
  inventoryDurationRangeMinute: number
  noTimeNeeded: boolean
  extraPricingFactor: any[]
  maxAllowed: number
  name: null
  category: string
  totalNumber: number
  isTicketBased: boolean
  givenNumber: number
  bulkAllowed: boolean
  individualAllowed: boolean
  capacity: number
}

export interface AvailabilityPayloadType {
  booked_for: string
  booked_until: string
  is_bulk_booking: boolean
  people_attending: PeopleAttendingType[]
  service_and_provider_id: number | null
  inventory_id: number | null
  time_unit: string
  extra_pricing_list: number[]
  paying_currency?: string
}

export interface PeopleAttendingType {
  id: number
  age_group: string
  is_student: boolean
  nationality: string
  no_of_people: number
  no_of_ticket: number
}

export interface BookingResponseType {
  txnId: string
  id: number
  guid: string
  totalAmount: string
  reservationSeconds: number
}

export interface AvailabilityResponse {
  remarks: string
  startFrom: string
  endTime: string
  isBulkBooking: boolean
  ticketInfo: string
  thumbnail: string
  serviceAndProviderId: number
  inventoryId: number
  category: string
  serviceType: string
  service: string
  timeUnit: string
  duration: number
  bookingDate: string
  priceInfo: PriceInfo
  allRanges: any[]
}

export interface PriceInfo {
  totalNprPrice: number
  totalPriceAfterDiscount: number
  totalUsdPrice: number
  totalDiscount: number
  loyaltyCoin: number
  detailCost: DetailCost[]
}

export interface DetailCost {
  name: string
  ageGroup: string
  nationality: string
  noOfPeople: number
  noOfTicket: number
  isStudent: boolean
  totalNprPrice: number
  totalUsdPrice: number
  extraPricings: any[]
  discountPrice: number
}
