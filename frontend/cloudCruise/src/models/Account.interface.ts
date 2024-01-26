export interface UserDataModel {
  firstName: string
  lastName: string
  email: string
  totalRewardCoin: string
  username: string
  avatar: string
}

export interface userEditModal {
  firstName: string
  lastName: string
}

export interface SelectOptionType {
  label: string
  value: string
  disabled?: boolean
}

export interface PaidFor {
  domestic: Domestic[]
  activity: any[]
}

export interface Domestic {
  airline: string
}

export interface TransactionType {
  id: number
  paidFor: PaidFor
  invoiceUrl: string
  dateCreated: Date
  dateModified: Date
  paymentMethod: string
  paymentProvidersTxnId: string
  paymentMethodName: string
  discount: string
  tax: string
  status: string
  totalAmount: string
  currency: null
  totalCommissionedAmount: string
  paidAmount: string
  txnId: string
  user: number
  billingAddress: null
}
