export interface FlightSearchPayload {
  adultPassenger: number
  childPassenger: number
  departureDate: string | null
  destinationLocationCode: string | null
  originLocationCode: string | null
  nationality: string
  seatClass: string
  returnFlight: boolean
  returnDate?: string
}
export interface CountryCode {
  name: string
  prefix: string
  code: string
}
export interface SectorCode {
  value: string
  label: string
}
export interface FlightComponentDetails {
  airline: string
  airlineLogo: string
  flightDate: Date
  flightNo: string
  departure: string
  departureTime: string
  arrival: string
  arrivalTime: string
  aircraftType: string
  adult: string
  child: string
  infant: string
  flightId: string
  flightClassCode: string
  currency: string
  adultFare: string
  childFare: string
  infantFare: string
  resFare: string
  fuelSurcharge: string
  tax: string
  adultVAT: string
  childVAT: string
  refundable: string
  freeBaggage: string
  agencyCommission: string
  childCommission: string
  elapsedTime: string
  timeUnit: string
  arrivalCode: string
  departureCode: string
  airlineName: string
  totalPeople: number
  totalCommissionedCost: number
  totalPrice: number
  discountAmount: number
  discountFor: string
  rewardCoins: number
}

export interface FlightList {
  airline: string
  airlineLogo: string
  flightDate: string
  flightNo: string
  departure: string
  departureTime: string
  arrival: string
  arrivalTime: string
  aircraftType: string
  adult: string | null
  child: string | null
  infant: string
  flightId: string
  flightClassCode: string
  currency: string
  adultFare: string
  childFare: string
  infantFare: string
  resFare: string
  fuelSurcharge: string
  tax: string
  refundable: string
  freeBaggage: string
  agencyCommission: string
  childCommission: string
  elapsedTime: string
  timeUnit: string
  arrivalCode: string
  departureCode: string
  airlineName: string
  totalPeople: number
  totalCommissionedCost: number
  totalPrice: number
  discountAmount: number
  duration?: number
}

export interface FlightDetailResponse {
  flightInfo: FlightList[]
  totalCost: number
}

type StringOrNull = string | null
export interface PassengerDetail {
  first_name: StringOrNull
  gender: StringOrNull
  last_name: StringOrNull
  nationality: StringOrNull
  passenger_title: StringOrNull
  passenger_type: StringOrNull
}

export interface BookingPayload {
  flight_id: string | null
  passenger_details: PassengerDetail[]
}

export interface FlightBookingPayload {
  contactName: string
  contactEmail: string
  billing_address?: number | null
  contactMobile: string | null
  bookings: BookingPayload[]
}

export interface BillingListModel {
  id: number
  dateCreated: Date
  dateModified: Date
  name: string
  panOrVatNum: number
  address: string
}

export interface DomesticFlightTicketType {
  id: number
  airlineLogo: string
  ticketUrl: string
  airline: string
  departureFullName: string
  arrivalFullName: string
  firstName: string
  lastName: string
  passengerType: string
  passengerTitle: string
  nationality: string
  gender: string
  flightDate: string
  issuedDate: string
  issuedBy: string
  arrivalDestination: string
  departureDestination: string
  arrivalTime: string
  classCode: string
  refundable: string
  flightNo: string
  flightTime: string
  baggage: string
  fareAmount: string
  fareCurrency: string
  taxAmount: string
  taxCurrency: string
  surcharge: string
  commissionPlasma: string
  discountAmount: string
  costAfterDiscount: string
  pnrNo: string
  ticketNo: string
  totalCommissionedCost: string
  status: string
  user: number
  booking: number
  supportTicket: any
}

export interface ActivityTicketType {
  id: number
  ticketUrl: string
  dateCreated: string
  guid: string
  forDate: string
  bookingDate: string
  isDelivered: boolean
  nationality: string
  ageGroup: string
  isStudent: boolean
  scannedDate: string
  booking: number
}

export interface SelectedFlightType {
  departureFlight?: FlightList
  returnFlight?: FlightList
}

export interface AgodaTicketType {
  id: number
  ticketUrl: string
  dateCreated: Date
  leadGuest: string
  guid: string
  checkIn: Date
  checkOut: Date
  booking: number
  user: number
  hotel: number
}
