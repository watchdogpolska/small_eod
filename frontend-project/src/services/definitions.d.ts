// This file is generated, do not manually edit this file
// Update and use '@/scripts/generate_interface.js' instead

export interface AdministrativeUnit {
  id: string;
  parent: string | null;
  name: string;
  category: number;
  slug: string;
  updatedOn: string;
  active: boolean;
}

export interface AdministrativeUnitAutocomplete {
  id: string;
  name: string;
}

export interface CaseAutocomplete {
  id: number;
  name: string;
}

export interface ChannelAutocomplete {
  id: number;
  name: string;
}

export interface DocumentTypeAutocomplete {
  id: number;
  name: string;
}

export interface FeatureOptionAutocomplete {
  id: number;
  name: string;
}

export interface InstitutionAutocomplete {
  id: number;
  name: string;
}

export interface TagAutocomplete {
  id: number;
  name: string;
}

export interface UserAutocomplete {
  id: number;
  username: string;
}

export interface CaseList {
  id: number;
  comment: string;
  auditedInstitutions: string[];
  name: string;
  featureoptions: string[];
  tags: string[];
  createdOn: string;
  modifiedOn: string;
  letterCount: number;
}

export interface CaseCount {
  id: number;
  comment: string;
  auditedInstitutions: number[];
  name: string;
  responsibleUsers: number[];
  notifiedUsers: number[];
  featureoptions: number[];
  tags: string[];
  createdBy: number;
  modifiedBy: number;
  createdOn: string;
  modifiedOn: string;
  letterCount: number;
  noteCount: number;
  eventCount: number;
}

export interface User {
  password: string;
  username: string;
  email: string;
  firstName: string;
  lastName: string;
  id: number;
}

export interface Channel {
  id: number;
  name: string;
  city: boolean;
  voivodeship: boolean;
  flatNo: boolean;
  street: boolean;
  postalCode: boolean;
  houseNo: boolean;
  email: boolean;
  epuap: boolean;
}

export interface Collection {
  id: number;
  name: string;
  comment: string;
  public: boolean;
  expiredOn: string;
  query: string;
}

export interface Case {
  id: number;
  comment: string;
  auditedInstitutions: number[];
  name: string;
  responsibleUsers: number[];
  notifiedUsers: number[];
  featureoptions: number[];
  tags: string[];
  createdBy: number;
  modifiedBy: number;
  createdOn: string;
  modifiedOn: string;
}

export interface Event {
  id: number;
  case: number;
  name: string;
  date: string;
  comment: string;
}

export interface File {
  id: number;
  path: string;
  downloadUrl: string;
  name: string;
  letter: number;
}

export interface Letter {
  id: number;
  direction: string;
  channel: number;
  final: boolean;
  date: string;
  referenceNumber: string;
  institution: number;
  case: number;
  attachments: File[];
  comment: string;
  excerpt: string;
  documentType: number;
  createdOn: string;
  createdBy: number;
  modifiedOn: string;
  modifiedBy: number;
}

export interface Note {
  id: number;
  case: number;
  comment: string;
}

export interface TokenSet {
  lifetime: number;
  accessToken: string;
}

export interface DocumentType {
  id: number;
  name: string;
}

export interface EventList {
  id: number;
  case: string;
  name: string;
  date: string;
  comment: string;
}

export interface FeatureOption {
  id: number;
  name: string;
  feature: number;
}

export interface Feature {
  id: number;
  name: string;
  minOptions: number;
  maxOptions: number;
  featureoptions: number[];
}

export interface Institution {
  id: number;
  modifiedBy: number;
  createdBy: number;
  modifiedOn: string;
  createdOn: string;
  name: string;
  administrativeUnit: string;
  email: string;
  city: string;
  epuap: string;
  street: string;
  houseNo: string;
  postalCode: string;
  flatNo: string;
  nip: string;
  regon: string;
  comment: string;
  tags: string[];
}

export interface LetterList {
  id: number;
  direction: string;
  channel: string;
  final: boolean;
  date: string;
  referenceNumber: string;
  institution: string;
  case: string;
  attachmentsCount: number;
  comment: string;
  documentType: string;
  createdOn: string;
  modifiedOn: string;
}

export interface SignRequest {
  name: string;
  method: string;
  url: string;
  formData: unknown;
  path: string;
}

export interface NoteList {
  id: number;
  case: string;
  comment: string;
}

export interface Tag {
  id: number;
  name: string;
}

export interface Request {
  url: string;
}

export interface TokenResponse {
  accessToken: string;
  expiresIn: number;
  refreshToken: string;
}

export interface RefreshTokenRequest {
  refreshToken: string;
}
