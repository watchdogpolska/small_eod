import smallEodSDK from '@/utils/sdk';
import { PaginationParams } from './common';
import {
  AdministrativeUnitAutocomplete,
  CaseAutocomplete,
  ChannelAutocomplete,
  DocumentTypeAutocomplete,
  FeatureOptionAutocomplete,
  InstitutionAutocomplete,
  TagAutocomplete,
  UserAutocomplete,
} from './definitions';

const api = new smallEodSDK.AutocompleteApi();

export type AutocompleteFunctionType<T> = (props: PaginationParams) => Promise<T[]>;

export type AutocompleteServiceType = {
  administrativeUnits: AutocompleteFunctionType<AdministrativeUnitAutocomplete>;
  cases: AutocompleteFunctionType<CaseAutocomplete>;
  channels: AutocompleteFunctionType<ChannelAutocomplete>;
  documentTypes: AutocompleteFunctionType<DocumentTypeAutocomplete>;
  features: AutocompleteFunctionType<FeatureOptionAutocomplete>;
  featureOptions: AutocompleteFunctionType<FeatureOptionAutocomplete>;
  institutions: AutocompleteFunctionType<InstitutionAutocomplete>;
  tags: AutocompleteFunctionType<TagAutocomplete>;
  users: AutocompleteFunctionType<UserAutocomplete>;
};

export const AutocompleteService: AutocompleteServiceType = {
  administrativeUnits: async props =>
    (await api.autocompleteAdministrativeUnitsList(props)).results,
  cases: async props => (await api.autocompleteCasesList(props)).results,
  channels: async props => (await api.autocompleteChannelsList(props)).results,
  documentTypes: async props => (await api.autocompleteDocumentTypesList(props)).results,
  features: async props => (await api.autocompleteFeaturesList(props)).results,
  featureOptions: async props => (await api.autocompleteFeatureOptionsList(props)).results,
  institutions: async props => (await api.autocompleteInstitutionsList(props)).results,
  tags: async props => (await api.autocompleteTagsList(props)).results,
  users: async props => (await api.autocompleteUsersList(props)).results,
};
