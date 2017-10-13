| Action | Foreman API | Description |
|--------|-------------|-------------|
| activation_keys_add_host_collections | [POST /katello/api/activation_keys/:id/host_collections](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/add_host_collections.html)  |  |
| activation_keys_add_subscriptions | [PUT /katello/api/activation_keys/:id/add_subscriptions](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/add_subscriptions.html)  | Attach a subscription |
| activation_keys_available_host_collections | [GET /katello/api/activation_keys/:id/host_collections/available](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/available_host_collections.html)  | List host collections the system does not belong to |
| activation_keys_available_releases | [GET /katello/api/activation_keys/:id/releases](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/available_releases.html)  | Show release versions available for an activation key |
| activation_keys_content_override | [PUT /katello/api/activation_keys/:id/content_override](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/content_override.html)  | Override content for activation_key |
| activation_keys_copy | [POST /katello/api/activation_keys/:id/copy](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/copy.html)  | Copy an activation key |
| activation_keys_create | [POST /katello/api/activation_keys](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/create.html)  | Create an activation key |
| activation_keys_destroy | [DELETE /katello/api/activation_keys/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/destroy.html)  | Destroy an activation key |
| activation_keys_host_collections_index | [GET /katello/api/activation_keys/:activation_key_id/host_collections](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/host_collections/index.html)  | List host collections in an activation key |
| activation_keys_index | [GET /katello/api/activation_keys](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/index.html)  | List activation keys |
| activation_keys_product_content | [GET /katello/api/activation_keys/:id/product_content](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/product_content.html)  | Show content available for an activation key |
| activation_keys_products_index | [GET /katello/api/activation_keys/:activation_key_id/products](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/products/index.html)  | List of subscription products in an activation key |
| activation_keys_remove_host_collections | [PUT /katello/api/activation_keys/:id/host_collections](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/remove_host_collections.html)  |  |
| activation_keys_remove_subscriptions | [PUT /katello/api/activation_keys/:id/remove_subscriptions](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/remove_subscriptions.html)  | Unattach a subscription |
| activation_keys_show | [GET /katello/api/activation_keys/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/show.html)  | Show an activation key |
| activation_keys_subscriptions_create | [POST /katello/api/activation_keys/:activation_key_id/subscriptions](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/subscriptions/create.html)  | Add a subscription to an activation key |
| activation_keys_subscriptions_ctivation_destroykeys | [DELETE /katello/api/activation_keys/:activation_key_id/subscriptions/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/subscriptions/destroy.html)  | Unattach a subscription |
| activation_keys_subscriptions_index | [GET /katello/api/activation_keys/:activation_key_id/subscriptions](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/subscriptions/index.html)  | List an activation key's subscriptions |
| activation_keys_update | [PUT /katello/api/activation_keys/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/update.html)  | Update an activation key |
| api_home_index | [GET /api](https://theforeman.org/api/1.16/apidoc/v2/home/index.html)  | Show available API links |
| architectures_create | [POST /api/architectures](https://theforeman.org/api/1.16/apidoc/v2/architectures/create.html)  | Create an architecture |
| architectures_destroy | [DELETE /api/architectures/:id](https://theforeman.org/api/1.16/apidoc/v2/architectures/destroy.html)  | Delete an architecture |
| architectures_images_architecture_id_showimages | [GET /api/architectures/:architecture_id/images/:id](https://theforeman.org/api/1.16/apidoc/v2/images/show.html)  | Show an image |
| architectures_images_index | [GET /api/architectures/:architecture_id/images](https://theforeman.org/api/1.16/apidoc/v2/images/index.html)  | List all images for architecture |
| architectures_index | [GET /api/architectures](https://theforeman.org/api/1.16/apidoc/v2/architectures/index.html)  | List all architectures |
| architectures_operatingsystems_index | [GET /api/architectures/:architecture_id/operatingsystems](https://theforeman.org/api/1.16/apidoc/v2/operatingsystems/index.html)  | List all operating systems for nested architecture |
| architectures_show | [GET /api/architectures/:id](https://theforeman.org/api/1.16/apidoc/v2/architectures/show.html)  | Show an architecture |
| architectures_update | [PUT /api/architectures/:id](https://theforeman.org/api/1.16/apidoc/v2/architectures/update.html)  | Update an architecture |
| audits_index | [GET /api/audits](https://theforeman.org/api/1.16/apidoc/v2/audits/index.html)  | List all audits |
| audits_show | [GET /api/audits/:id](https://theforeman.org/api/1.16/apidoc/v2/audits/show.html)  | Show an audit |
| auth_source_ldaps_create | [POST /api/auth_source_ldaps](https://theforeman.org/api/1.16/apidoc/v2/auth_source_ldaps/create.html)  | Create an LDAP authentication source |
| auth_source_ldaps_destroy | [DELETE /api/auth_source_ldaps/:id](https://theforeman.org/api/1.16/apidoc/v2/auth_source_ldaps/destroy.html)  | Delete an LDAP authentication source |
| auth_source_ldaps_external_usergroups_auth_source_ldap_id_external_showusergroups | [GET /api/auth_source_ldaps/:auth_source_ldap_id/external_usergroups/:id](https://theforeman.org/api/1.16/apidoc/v2/external_usergroups/show.html)  | Show an external user group for LDAP authentication source |
| auth_source_ldaps_external_usergroups_index | [GET /api/auth_source_ldaps/:auth_source_ldap_id/external_usergroups](https://theforeman.org/api/1.16/apidoc/v2/external_usergroups/index.html)  | List all external user groups for LDAP authentication source |
| auth_source_ldaps_index | [GET /api/auth_source_ldaps](https://theforeman.org/api/1.16/apidoc/v2/auth_source_ldaps/index.html)  | List all LDAP authentication sources |
| auth_source_ldaps_show | [GET /api/auth_source_ldaps/:id](https://theforeman.org/api/1.16/apidoc/v2/auth_source_ldaps/show.html)  | Show an LDAP authentication source |
| auth_source_ldaps_test | [PUT /api/auth_source_ldaps/:id/test](https://theforeman.org/api/1.16/apidoc/v2/auth_source_ldaps/test.html)  | Test LDAP connection |
| auth_source_ldaps_update | [PUT /api/auth_source_ldaps/:id](https://theforeman.org/api/1.16/apidoc/v2/auth_source_ldaps/update.html)  | Update an LDAP authentication source |
| auth_source_ldaps_users_index | [GET /api/auth_source_ldaps/:auth_source_ldap_id/users](https://theforeman.org/api/1.16/apidoc/v2/users/index.html)  | List all users for LDAP authentication source |
| bookmarks_create | [POST /api/bookmarks](https://theforeman.org/api/1.16/apidoc/v2/bookmarks/create.html)  | Create a bookmark |
| bookmarks_destroy | [DELETE /api/bookmarks/:id](https://theforeman.org/api/1.16/apidoc/v2/bookmarks/destroy.html)  | Delete a bookmark |
| bookmarks_index | [GET /api/bookmarks](https://theforeman.org/api/1.16/apidoc/v2/bookmarks/index.html)  | List all bookmarks |
| bookmarks_show | [GET /api/bookmarks/:id](https://theforeman.org/api/1.16/apidoc/v2/bookmarks/show.html)  | Show a bookmark |
| bookmarks_update | [PUT /api/bookmarks/:id](https://theforeman.org/api/1.16/apidoc/v2/bookmarks/update.html)  | Update a bookmark |
| capsules_capsule_content_add_lifecycle_environment | [POST /katello/api/capsules/:id/content/lifecycle_environments](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/capsule_content/add_lifecycle_environment.html)  | Add lifecycle environments to the capsule |
| capsules_capsule_content_apsules | [DELETE /katello/api/capsules/:id/content/lifecycle_environments/:environment_id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/capsule_content/remove_lifecycle_environment.html)  | Remove lifecycle environments from the capsule |
| capsules_capsule_content_available_lifecycle_environments | [GET /katello/api/capsules/:id/content/available_lifecycle_environments](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/capsule_content/available_lifecycle_environments.html)  | List the lifecycle environments not attached to the capsule |
| capsules_capsule_content_cancel_sync | [DELETE /katello/api/capsules/:id/content/sync](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/capsule_content/cancel_sync.html)  | Cancel running capsule synchronization. |
| capsules_capsule_content_lifecycle_environments | [GET /katello/api/capsules/:id/content/lifecycle_environments](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/capsule_content/lifecycle_environments.html)  | List the lifecycle environments attached to the capsule |
| capsules_capsule_content_sync | [POST /katello/api/capsules/:id/content/sync](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/capsule_content/sync.html)  | Synchronize the content to the capsule |
| capsules_capsule_content_sync_status | [GET /katello/api/capsules/:id/content/sync](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/capsule_content/sync_status.html)  | Get current capsule synchronization status |
| capsules_index | [GET /katello/api/capsules](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/capsules/index.html)  | List all capsules |
| capsules_show | [GET /katello/api/capsules/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/capsules/show.html)  | Show the capsule details |
| common_parameters_create | [POST /api/common_parameters](https://theforeman.org/api/1.16/apidoc/v2/common_parameters/create.html)  | Create a global parameter |
| common_parameters_destroy | [DELETE /api/common_parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/common_parameters/destroy.html)  | Delete a global parameter |
| common_parameters_index | [GET /api/common_parameters](https://theforeman.org/api/1.16/apidoc/v2/common_parameters/index.html)  | List all global parameters. |
| common_parameters_show | [GET /api/common_parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/common_parameters/show.html)  | Show a global parameter |
| common_parameters_update | [PUT /api/common_parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/common_parameters/update.html)  | Update a global parameter |
| compare_docker_manifests_compare | [GET /katello/api/compare](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_manifests/compare.html)  | List docker_manifests |
| compare_docker_tags_compare | [GET /katello/api/compare](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_tags/compare.html)  | List docker_tags |
| compare_errata_compare | [GET /katello/api/compare](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/errata/compare.html)  | List errata |
| compare_ostree_branches_compare | [GET /katello/api/compare](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/ostree_branches/compare.html)  | List ostree_branches |
| compare_package_groups_compare | [GET /katello/api/compare](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/package_groups/compare.html)  | List package_groups |
| compare_packages_compare | [GET /katello/api/compare](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/packages/compare.html)  | List packages |
| compare_puppet_modules_compare | [GET /katello/api/compare](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/puppet_modules/compare.html)  | List puppet_modules |
| compliance_foreman_openscap_arf_reports_destroy | [DELETE /api/v2/compliance/arf_reports/:id](https://theforeman.org/api/1.16/apidoc/v2/foreman_openscap_arf_reports/destroy.html)  | Deletes an Arf Report |
| compliance_foreman_openscap_arf_reports_index | [GET /api/v2/compliance/arf_reports](https://theforeman.org/api/1.16/apidoc/v2/foreman_openscap_arf_reports/index.html)  | List Arf reports |
| compliance_foreman_openscap_arf_reports_ompliance_createarf | [POST /api/v2/compliance/arf/:cname/:policy_id/:date](https://theforeman.org/api/1.16/apidoc/v2/foreman_openscap_arf_reports/create.html)  | Upload an ARF report |
| compliance_foreman_openscap_arf_reports_show | [GET /api/v2/compliance/arf_reports/:id](https://theforeman.org/api/1.16/apidoc/v2/foreman_openscap_arf_reports/show.html)  | Show an Arf report |
| compliance_foreman_openscap_policies_content | [GET /api/v2/compliance/policies/:id/content](https://theforeman.org/api/1.16/apidoc/v2/foreman_openscap_policies/content.html)  | Show a policy's SCAP content |
| compliance_foreman_openscap_policies_create | [POST /api/v2/compliance/policies](https://theforeman.org/api/1.16/apidoc/v2/foreman_openscap_policies/create.html)  | Create a policy |
| compliance_foreman_openscap_policies_destroy | [DELETE /api/v2/compliance/policies/:id](https://theforeman.org/api/1.16/apidoc/v2/foreman_openscap_policies/destroy.html)  | Deletes a policy |
| compliance_foreman_openscap_policies_index | [GET /api/v2/compliance/policies](https://theforeman.org/api/1.16/apidoc/v2/foreman_openscap_policies/index.html)  | List SCAP contents |
| compliance_foreman_openscap_policies_show | [GET /api/v2/compliance/policies/:id](https://theforeman.org/api/1.16/apidoc/v2/foreman_openscap_policies/show.html)  | Show an SCAP content |
| compliance_foreman_openscap_policies_update | [PUT /api/v2/compliance/policies/:id](https://theforeman.org/api/1.16/apidoc/v2/foreman_openscap_policies/update.html)  | Update a policy |
| compliance_foreman_openscap_scap_contents_create | [POST /api/v2/compliance/scap_contents](https://theforeman.org/api/1.16/apidoc/v2/foreman_openscap_scap_contents/create.html)  | Create SCAP content |
| compliance_foreman_openscap_scap_contents_destroy | [DELETE /api/v2/compliance/scap_contents/:id](https://theforeman.org/api/1.16/apidoc/v2/foreman_openscap_scap_contents/destroy.html)  | Deletes an SCAP content |
| compliance_foreman_openscap_scap_contents_index | [GET /api/v2/compliance/scap_contents](https://theforeman.org/api/1.16/apidoc/v2/foreman_openscap_scap_contents/index.html)  | List SCAP contents |
| compliance_foreman_openscap_scap_contents_show | [GET /api/v2/compliance/scap_contents/:id](https://theforeman.org/api/1.16/apidoc/v2/foreman_openscap_scap_contents/show.html)  | Show an SCAP content |
| compliance_foreman_openscap_scap_contents_update | [PUT /api/v2/compliance/scap_contents/:id](https://theforeman.org/api/1.16/apidoc/v2/foreman_openscap_scap_contents/update.html)  | Update an SCAP content |
| compute_attributes_create | [POST /api/compute_attributes](https://theforeman.org/api/1.16/apidoc/v2/compute_attributes/create.html)  | Create a compute attributes set |
| compute_attributes_update | [PUT /api/compute_attributes/:id](https://theforeman.org/api/1.16/apidoc/v2/compute_attributes/update.html)  | Update a compute attributes set |
| compute_profiles_compute_attributes_compute_profile_id_compute_createresources | [POST /api/compute_profiles/:compute_profile_id/compute_resources/:compute_resource_id/compute_attributes](https://theforeman.org/api/1.16/apidoc/v2/compute_attributes/create.html)  | Create a compute attributes set |
| compute_profiles_compute_attributes_compute_profile_id_compute_updateattributes | [PUT /api/compute_profiles/:compute_profile_id/compute_attributes/:id](https://theforeman.org/api/1.16/apidoc/v2/compute_attributes/update.html)  | Update a compute attributes set |
| compute_profiles_compute_attributes_compute_profile_id_compute_updateresources | [PUT /api/compute_profiles/:compute_profile_id/compute_resources/:compute_resource_id/compute_attributes/:id](https://theforeman.org/api/1.16/apidoc/v2/compute_attributes/update.html)  | Update a compute attributes set |
| compute_profiles_compute_attributes_create | [POST /api/compute_profiles/:compute_profile_id/compute_attributes](https://theforeman.org/api/1.16/apidoc/v2/compute_attributes/create.html)  | Create a compute attributes set |
| compute_profiles_create | [POST /api/compute_profiles](https://theforeman.org/api/1.16/apidoc/v2/compute_profiles/create.html)  | Create a compute profile |
| compute_profiles_destroy | [DELETE /api/compute_profiles/:id](https://theforeman.org/api/1.16/apidoc/v2/compute_profiles/destroy.html)  | Delete a compute profile |
| compute_profiles_index | [GET /api/compute_profiles](https://theforeman.org/api/1.16/apidoc/v2/compute_profiles/index.html)  | List of compute profiles |
| compute_profiles_show | [GET /api/compute_profiles/:id](https://theforeman.org/api/1.16/apidoc/v2/compute_profiles/show.html)  | Show a compute profile |
| compute_profiles_update | [PUT /api/compute_profiles/:id](https://theforeman.org/api/1.16/apidoc/v2/compute_profiles/update.html)  | Update a compute profile |
| compute_resources_associate | [PUT /api/compute_resources/:id/associate](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/associate.html)  | Associate VMs to Hosts |
| compute_resources_available_clusters | [GET /api/compute_resources/:id/available_clusters](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/available_clusters.html)  | List available clusters for a compute resource |
| compute_resources_available_flavors | [GET /api/compute_resources/:id/available_flavors](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/available_flavors.html)  | List available flavors for a compute resource |
| compute_resources_available_folders | [GET /api/compute_resources/:id/available_folders](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/available_folders.html)  | List available folders for a compute resource |
| compute_resources_available_images | [GET /api/compute_resources/:id/available_images](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/available_images.html)  | List available images for a compute resource |
| compute_resources_available_networks | [GET /api/compute_resources/:id/available_networks](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/available_networks.html)  | List available networks for a compute resource |
| compute_resources_available_security_groups | [GET /api/compute_resources/:id/available_security_groups](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/available_security_groups.html)  | List available security groups for a compute resource |
| compute_resources_available_storage_domains | [GET /api/compute_resources/:id/available_storage_domains](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/available_storage_domains.html)  | List storage domains for a compute resource |
| compute_resources_available_storage_pods | [GET /api/compute_resources/:id/available_storage_pods](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/available_storage_pods.html)  | List storage pods for a compute resource |
| compute_resources_available_zones | [GET /api/compute_resources/:id/available_zones](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/available_zones.html)  | List available zone for a compute resource |
| compute_resources_compute_attributes_compute_resource_id_compute_createprofiles | [POST /api/compute_resources/:compute_resource_id/compute_profiles/:compute_profile_id/compute_attributes](https://theforeman.org/api/1.16/apidoc/v2/compute_attributes/create.html)  | Create a compute attributes set |
| compute_resources_compute_attributes_compute_resource_id_compute_updateattributes | [PUT /api/compute_resources/:compute_resource_id/compute_attributes/:id](https://theforeman.org/api/1.16/apidoc/v2/compute_attributes/update.html)  | Update a compute attributes set |
| compute_resources_compute_attributes_compute_resource_id_compute_updateprofiles | [PUT /api/compute_resources/:compute_resource_id/compute_profiles/:compute_profile_id/compute_attributes/:id](https://theforeman.org/api/1.16/apidoc/v2/compute_attributes/update.html)  | Update a compute attributes set |
| compute_resources_compute_attributes_create | [POST /api/compute_resources/:compute_resource_id/compute_attributes](https://theforeman.org/api/1.16/apidoc/v2/compute_attributes/create.html)  | Create a compute attributes set |
| compute_resources_create | [POST /api/compute_resources](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/create.html)  | Create a compute resource |
| compute_resources_destroy | [DELETE /api/compute_resources/:id](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/destroy.html)  | Delete a compute resource |
| compute_resources_id_available_available_networksclusters | [GET /api/compute_resources/:id/available_clusters/:cluster_id/available_networks](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/available_networks.html)  | List available networks for a compute resource cluster |
| compute_resources_id_available_available_resource_poolsclusters | [GET /api/compute_resources/:id/available_clusters/:cluster_id/available_resource_pools](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/available_resource_pools.html)  | List resource pools for a compute resource cluster |
| compute_resources_id_available_storage_available_storage_domainsdomains | [GET /api/compute_resources/:id/available_storage_domains/:storage_domain](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/available_storage_domains.html)  | List attributes for a given storage domain |
| compute_resources_id_available_storage_available_storage_podspods | [GET /api/compute_resources/:id/available_storage_pods/:storage_pod](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/available_storage_pods.html)  | List attributes for a given storage pod |
| compute_resources_images_compute_resource_id_destroyimages | [DELETE /api/compute_resources/:compute_resource_id/images/:id](https://theforeman.org/api/1.16/apidoc/v2/images/destroy.html)  | Delete an image |
| compute_resources_images_compute_resource_id_showimages | [GET /api/compute_resources/:compute_resource_id/images/:id](https://theforeman.org/api/1.16/apidoc/v2/images/show.html)  | Show an image |
| compute_resources_images_compute_resource_id_updateimages | [PUT /api/compute_resources/:compute_resource_id/images/:id](https://theforeman.org/api/1.16/apidoc/v2/images/update.html)  | Update an image |
| compute_resources_images_create | [POST /api/compute_resources/:compute_resource_id/images](https://theforeman.org/api/1.16/apidoc/v2/images/create.html)  | Create an image |
| compute_resources_images_index | [GET /api/compute_resources/:compute_resource_id/images](https://theforeman.org/api/1.16/apidoc/v2/images/index.html)  | List all images for a compute resource |
| compute_resources_index | [GET /api/compute_resources](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/index.html)  | List all compute resources |
| compute_resources_show | [GET /api/compute_resources/:id](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/show.html)  | Show a compute resource |
| compute_resources_update | [PUT /api/compute_resources/:id](https://theforeman.org/api/1.16/apidoc/v2/compute_resources/update.html)  | Update a compute resource |
| config_groups_create | [POST /api/config_groups](https://theforeman.org/api/1.16/apidoc/v2/config_groups/create.html)  | Create a config group |
| config_groups_destroy | [DELETE /api/config_groups/:id](https://theforeman.org/api/1.16/apidoc/v2/config_groups/destroy.html)  | Delete a config group |
| config_groups_index | [GET /api/config_groups](https://theforeman.org/api/1.16/apidoc/v2/config_groups/index.html)  | List of config groups |
| config_groups_show | [GET /api/config_groups/:id](https://theforeman.org/api/1.16/apidoc/v2/config_groups/show.html)  | Show a config group |
| config_groups_update | [PUT /api/config_groups/:id](https://theforeman.org/api/1.16/apidoc/v2/config_groups/update.html)  | Update a config group |
| config_reports_create | [POST /api/config_reports](https://theforeman.org/api/1.16/apidoc/v2/config_reports/create.html)  | Create a report |
| config_reports_destroy | [DELETE /api/config_reports/:id](https://theforeman.org/api/1.16/apidoc/v2/config_reports/destroy.html)  | Delete a report |
| config_reports_index | [GET /api/config_reports](https://theforeman.org/api/1.16/apidoc/v2/config_reports/index.html)  | List all reports |
| config_reports_show | [GET /api/config_reports/:id](https://theforeman.org/api/1.16/apidoc/v2/config_reports/show.html)  | Show a report |
| config_templates_build_pxe_default | [POST /api/config_templates/build_pxe_default](https://theforeman.org/api/1.16/apidoc/v2/config_templates/build_pxe_default.html)  | Update the default PXE menu on all configured TFTP servers |
| config_templates_clone | [POST /api/config_templates/:id/clone](https://theforeman.org/api/1.16/apidoc/v2/config_templates/clone.html)  | Clone a provision template |
| config_templates_create | [POST /api/config_templates](https://theforeman.org/api/1.16/apidoc/v2/config_templates/create.html)  | Create a provisioning template |
| config_templates_destroy | [DELETE /api/config_templates/:id](https://theforeman.org/api/1.16/apidoc/v2/config_templates/destroy.html)  | Delete a provisioning template |
| config_templates_index | [GET /api/config_templates](https://theforeman.org/api/1.16/apidoc/v2/config_templates/index.html)  | List provisioning templates |
| config_templates_operatingsystems_index | [GET /api/config_templates/:config_template_id/operatingsystems](https://theforeman.org/api/1.16/apidoc/v2/operatingsystems/index.html)  | List all operating systems for nested provisioning template |
| config_templates_os_default_templates_index | [GET /api/config_templates/:config_template_id/os_default_templates](https://theforeman.org/api/1.16/apidoc/v2/os_default_templates/index.html)  | List operating systems where this template is set as a default |
| config_templates_revision | [GET /api/config_templates/revision](https://theforeman.org/api/1.16/apidoc/v2/config_templates/revision.html)  |  |
| config_templates_show | [GET /api/config_templates/:id](https://theforeman.org/api/1.16/apidoc/v2/config_templates/show.html)  | Show provisioning template details |
| config_templates_template_combinations_config_template_id_template_showcombinations | [GET /api/config_templates/:config_template_id/template_combinations/:id](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/show.html)  | Show template combination |
| config_templates_template_combinations_config_template_id_template_updatecombinations | [PUT /api/config_templates/:config_template_id/template_combinations/:id](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/update.html)  | Update template combination |
| config_templates_template_combinations_create | [POST /api/config_templates/:config_template_id/template_combinations](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/create.html)  | Add a template combination |
| config_templates_template_combinations_index | [GET /api/config_templates/:config_template_id/template_combinations](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/index.html)  | List template combination |
| config_templates_update | [PUT /api/config_templates/:id](https://theforeman.org/api/1.16/apidoc/v2/config_templates/update.html)  | Update a provisioning template |
| content_view_filters_content_view_filter_rules_create | [POST /katello/api/content_view_filters/:content_view_filter_id/rules](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_filter_rules/create.html)  | Create a filter rule. The parameters included should be based upon the filter type. |
| content_view_filters_content_view_filter_rules_index | [GET /katello/api/content_view_filters/:content_view_filter_id/rules](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_filter_rules/index.html)  | List filter rules |
| content_view_filters_content_view_filter_rules_ontent_view_destroyfilters | [DELETE /katello/api/content_view_filters/:content_view_filter_id/rules/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_filter_rules/destroy.html)  | Delete a filter rule |
| content_view_filters_content_view_filter_rules_ontent_view_showfilters | [GET /katello/api/content_view_filters/:content_view_filter_id/rules/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_filter_rules/show.html)  | Show filter rule info |
| content_view_filters_content_view_filter_rules_ontent_view_updatefilters | [PUT /katello/api/content_view_filters/:content_view_filter_id/rules/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_filter_rules/update.html)  | Update a filter rule. The parameters included should be based upon the filter type. |
| content_view_filters_create | [post /katello/api/content_view_filters](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_filters/create.html)  | create a filter for a content view |
| content_view_filters_destroy | [delete /katello/api/content_view_filters/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_filters/destroy.html)  | delete a filter |
| content_view_filters_docker_manifests_index | [GET /katello/api/content_view_filters/:content_view_filter_id/docker_manifests](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_manifests/index.html)  | List docker_manifests |
| content_view_filters_docker_tags_index | [GET /katello/api/content_view_filters/:content_view_filter_id/docker_tags](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_tags/index.html)  | List docker_tags |
| content_view_filters_index | [get /katello/api/content_view_filters](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_filters/index.html)  | list filters |
| content_view_filters_ostree_branches_index | [GET /katello/api/content_view_filters/:content_view_filter_id/ostree_branches](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/ostree_branches/index.html)  | List ostree_branches |
| content_view_filters_package_groups_index | [GET /katello/api/content_view_filters/:content_view_filter_id/package_groups](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/package_groups/index.html)  | List package_groups |
| content_view_filters_packages_index | [GET /katello/api/content_view_filters/:content_view_filter_id/packages](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/packages/index.html)  | List packages |
| content_view_filters_puppet_modules_index | [GET /katello/api/content_view_filters/:content_view_filter_id/puppet_modules](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/puppet_modules/index.html)  | List puppet_modules |
| content_view_filters_show | [get /katello/api/content_view_filters/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_filters/show.html)  | show filter info |
| content_view_filters_update | [put /katello/api/content_view_filters/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_filters/update.html)  | update a filter |
| content_view_versions_destroy | [DELETE /katello/api/content_view_versions/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_versions/destroy.html)  | Remove content view version |
| content_view_versions_export | [POST /katello/api/content_view_versions/:id/export](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_versions/export.html)  | Export a content view version |
| content_view_versions_incremental_update | [POST /katello/api/content_view_versions/incremental_update](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_versions/incremental_update.html)  | Perform an Incremental Update on one or more Content View Versions |
| content_view_versions_index | [GET /katello/api/content_view_versions](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_versions/index.html)  | List content view versions |
| content_view_versions_promote | [POST /katello/api/content_view_versions/:id/promote](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_versions/promote.html)  | Promote a content view version |
| content_view_versions_show | [GET /katello/api/content_view_versions/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_versions/show.html)  | Show content view version |
| content_views_available_puppet_module_names | [GET /katello/api/content_views/:id/available_puppet_module_names](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_views/available_puppet_module_names.html)  | Get puppet modules names that are available to be added to the content view |
| content_views_available_puppet_modules | [GET /katello/api/content_views/:id/available_puppet_modules](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_views/available_puppet_modules.html)  | Get puppet modules that are available to be added to the content view |
| content_views_content_view_filters_create | [post /katello/api/content_views/:content_view_id/filters](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_filters/create.html)  | create a filter for a content view |
| content_views_content_view_filters_index | [get /katello/api/content_views/:content_view_id/filters](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_filters/index.html)  | list filters |
| content_views_content_view_filters_ontent_destroyviews | [delete /katello/api/content_views/:content_view_id/filters/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_filters/destroy.html)  | delete a filter |
| content_views_content_view_filters_ontent_showviews | [get /katello/api/content_views/:content_view_id/filters/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_filters/show.html)  | show filter info |
| content_views_content_view_filters_ontent_updateviews | [put /katello/api/content_views/:content_view_id/filters/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_filters/update.html)  | update a filter |
| content_views_content_view_histories_index | [GET /katello/api/content_views/:id/history](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_histories/index.html)  | Show a content view's history |
| content_views_content_view_puppet_modules_create | [POST /katello/api/content_views/:content_view_id/content_view_puppet_modules](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_puppet_modules/create.html)  | Add a puppet module to the content view |
| content_views_content_view_puppet_modules_index | [GET /katello/api/content_views/:content_view_id/content_view_puppet_modules](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_puppet_modules/index.html)  | List content view puppet modules |
| content_views_content_view_puppet_modules_ontent_destroyviews | [DELETE /katello/api/content_views/:content_view_id/content_view_puppet_modules/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_puppet_modules/destroy.html)  | Remove a puppet module from the content view |
| content_views_content_view_puppet_modules_ontent_showviews | [GET /katello/api/content_views/:content_view_id/content_view_puppet_modules/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_puppet_modules/show.html)  | Show a content view puppet module |
| content_views_content_view_puppet_modules_ontent_updateviews | [PUT /katello/api/content_views/:content_view_id/content_view_puppet_modules/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_puppet_modules/update.html)  | Update a puppet module associated with the content view |
| content_views_content_view_versions_index | [GET /katello/api/content_views/:content_view_id/content_view_versions](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_view_versions/index.html)  | List content view versions |
| content_views_copy | [POST /katello/api/content_views/:id/copy](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_views/copy.html)  | Make copy of a content view |
| content_views_create | [POST /katello/api/content_views](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_views/create.html)  | Create a content view |
| content_views_destroy | [DELETE /katello/api/content_views/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_views/destroy.html)  | Delete a content view |
| content_views_docker_manifests_ontent_indexviews | [GET /katello/api/content_views/:content_view_id/filters/:filter_id/docker_manifests](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_manifests/index.html)  | List docker_manifests |
| content_views_docker_tags_ontent_indexviews | [GET /katello/api/content_views/:content_view_id/filters/:filter_id/docker_tags](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_tags/index.html)  | List docker_tags |
| content_views_index | [GET /katello/api/content_views](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_views/index.html)  | List content views |
| content_views_ontent_remove_from_environmentviews | [DELETE /katello/api/content_views/:id/environments/:environment_id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_views/remove_from_environment.html)  | Remove a content view from an environment |
| content_views_ostree_branches_ontent_indexviews | [GET /katello/api/content_views/:content_view_id/filters/:filter_id/ostree_branches](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/ostree_branches/index.html)  | List ostree_branches |
| content_views_package_groups_ontent_indexviews | [GET /katello/api/content_views/:content_view_id/filters/:filter_id/package_groups](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/package_groups/index.html)  | List package_groups |
| content_views_packages_ontent_indexviews | [GET /katello/api/content_views/:content_view_id/filters/:filter_id/packages](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/packages/index.html)  | List packages |
| content_views_publish | [POST /katello/api/content_views/:id/publish](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_views/publish.html)  | Publish a content view |
| content_views_puppet_modules_ontent_indexviews | [GET /katello/api/content_views/:content_view_id/filters/:filter_id/puppet_modules](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/puppet_modules/index.html)  | List puppet_modules |
| content_views_remove | [PUT /katello/api/content_views/:id/remove](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_views/remove.html)  | Remove versions and/or environments from a content view and reassign systems and keys |
| content_views_repositories_index | [GET /katello/api/content_views/:id/repositories](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/index.html)  | List of repositories for a content view |
| content_views_show | [GET /katello/api/content_views/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_views/show.html)  | Show a content view |
| content_views_update | [PUT /katello/api/content_views/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_views/update.html)  | Update a content view |
| dashboard_index | [GET /api/dashboard](https://theforeman.org/api/1.16/apidoc/v2/dashboard/index.html)  | Get dashboard details |
| discovered_hosts_auto_provision | [POST /api/v2/discovered_hosts/:id/auto_provision](https://theforeman.org/api/1.16/apidoc/v2/discovered_hosts/auto_provision.html)  | Execute rules against a discovered host |
| discovered_hosts_auto_provision_all | [POST /api/v2/discovered_hosts/auto_provision_all](https://theforeman.org/api/1.16/apidoc/v2/discovered_hosts/auto_provision_all.html)  | Execute rules against all currently discovered hosts |
| discovered_hosts_create | [POST /api/v2/discovered_hosts](https://theforeman.org/api/1.16/apidoc/v2/discovered_hosts/create.html)  | Create a discovered host for testing (use /facts to create new hosts) |
| discovered_hosts_destroy | [DELETE /api/v2/discovered_hosts/:id](https://theforeman.org/api/1.16/apidoc/v2/discovered_hosts/destroy.html)  | Delete a discovered host |
| discovered_hosts_facts | [POST /api/v2/discovered_hosts/facts](https://theforeman.org/api/1.16/apidoc/v2/discovered_hosts/facts.html)  | Upload facts for a host, creating the host if required |
| discovered_hosts_index | [GET /api/v2/discovered_hosts](https://theforeman.org/api/1.16/apidoc/v2/discovered_hosts/index.html)  | List all discovered hosts |
| discovered_hosts_reboot | [PUT /api/v2/discovered_hosts/:id/reboot](https://theforeman.org/api/1.16/apidoc/v2/discovered_hosts/reboot.html)  | Rebooting a discovered host |
| discovered_hosts_reboot_all | [PUT /api/v2/discovered_hosts/reboot_all](https://theforeman.org/api/1.16/apidoc/v2/discovered_hosts/reboot_all.html)  | Rebooting all discovered hosts |
| discovered_hosts_refresh_facts | [PUT /api/v2/discovered_hosts/:id/refresh_facts](https://theforeman.org/api/1.16/apidoc/v2/discovered_hosts/refresh_facts.html)  | Refreshing the facts of a discovered host |
| discovered_hosts_show | [GET /api/v2/discovered_hosts/:id](https://theforeman.org/api/1.16/apidoc/v2/discovered_hosts/show.html)  | Show a discovered host |
| discovered_hosts_update | [PUT /api/v2/discovered_hosts/:id](https://theforeman.org/api/1.16/apidoc/v2/discovered_hosts/update.html)  | Provision a discovered host |
| discovery_rules_create | [POST /api/v2/discovery_rules](https://theforeman.org/api/1.16/apidoc/v2/discovery_rules/create.html)  | Create a discovery rule |
| discovery_rules_destroy | [DELETE /api/v2/discovery_rules/:id](https://theforeman.org/api/1.16/apidoc/v2/discovery_rules/destroy.html)  | Delete a rule |
| discovery_rules_index | [GET /api/v2/discovery_rules](https://theforeman.org/api/1.16/apidoc/v2/discovery_rules/index.html)  | List all discovery rules |
| discovery_rules_show | [GET /api/v2/discovery_rules/:id](https://theforeman.org/api/1.16/apidoc/v2/discovery_rules/show.html)  | Show a discovery rule |
| discovery_rules_update | [PUT /api/v2/discovery_rules/:id](https://theforeman.org/api/1.16/apidoc/v2/discovery_rules/update.html)  | Update a rule |
| docker_manifests_index | [GET /katello/api/docker_manifests](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_manifests/index.html)  | List docker_manifests |
| docker_manifests_show | [GET /katello/api/docker_manifests/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_manifests/show.html)  | Show a docker manifest |
| docker_tags_index | [GET /katello/api/docker_tags](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_tags/index.html)  | List docker_tags |
| docker_tags_show | [GET /katello/api/docker_tags/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_tags/show.html)  | Show a docker tag |
| domains_create | [POST /api/domains](https://theforeman.org/api/1.16/apidoc/v2/domains/create.html)  | Create a domain |
| domains_destroy | [DELETE /api/domains/:id](https://theforeman.org/api/1.16/apidoc/v2/domains/destroy.html)  | Delete a domain |
| domains_index | [GET /api/domains](https://theforeman.org/api/1.16/apidoc/v2/domains/index.html)  | List of domains |
| domains_interfaces_index | [GET /api/domains/:domain_id/interfaces](https://theforeman.org/api/1.16/apidoc/v2/interfaces/index.html)  | List all interfaces for domain |
| domains_parameters_create | [POST /api/domains/:domain_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/create.html)  | Create a nested parameter for a domain |
| domains_parameters_domain_id_destroyparameters | [DELETE /api/domains/:domain_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/destroy.html)  | Delete a nested parameter for a domain |
| domains_parameters_domain_id_showparameters | [GET /api/domains/:domain_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/show.html)  | Show a nested parameter for a domain |
| domains_parameters_domain_id_updateparameters | [PUT /api/domains/:domain_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/update.html)  | Update a nested parameter for a domain |
| domains_parameters_index | [GET /api/domains/:domain_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/index.html)  | List all parameters for a domain |
| domains_parameters_reset | [DELETE /api/domains/:domain_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/reset.html)  | Delete all nested parameters for a domain |
| domains_show | [GET /api/domains/:id](https://theforeman.org/api/1.16/apidoc/v2/domains/show.html)  | Show a domain |
| domains_subnets_index | [GET /api/domains/:domain_id/subnets](https://theforeman.org/api/1.16/apidoc/v2/subnets/index.html)  | List of subnets for a domain |
| domains_update | [PUT /api/domains/:id](https://theforeman.org/api/1.16/apidoc/v2/domains/update.html)  | Update a domain |
| environments_activation_keys_index | [GET /katello/api/environments/:environment_id/activation_keys](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/index.html)  |  |
| environments_create | [POST /api/environments](https://theforeman.org/api/1.16/apidoc/v2/environments/create.html)  | Create an environment |
| environments_destroy | [DELETE /api/environments/:id](https://theforeman.org/api/1.16/apidoc/v2/environments/destroy.html)  | Delete an environment |
| environments_environment_id_smart_import_puppetclassesproxies | [POST /api/environments/:environment_id/smart_proxies/:id/import_puppetclasses](https://theforeman.org/api/1.16/apidoc/v2/environments/import_puppetclasses.html)  | Import puppet classes from puppet Capsule for an environment |
| environments_hosts_index | [GET /api/environments/:environment_id/hosts](https://theforeman.org/api/1.16/apidoc/v2/hosts/index.html)  | List hosts per environment |
| environments_index | [GET /api/environments](https://theforeman.org/api/1.16/apidoc/v2/environments/index.html)  | List all environments |
| environments_lifecycle_environments_create | [POST /katello/api/environments](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/lifecycle_environments/create.html)  | Create an environment |
| environments_lifecycle_environments_destroy | [DELETE /katello/api/environments/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/lifecycle_environments/destroy.html)  | Destroy an environment |
| environments_lifecycle_environments_index | [GET /katello/api/environments](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/lifecycle_environments/index.html)  | List environments in an organization |
| environments_lifecycle_environments_show | [GET /katello/api/environments/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/lifecycle_environments/show.html)  | Show an environment |
| environments_lifecycle_environments_update | [PUT /katello/api/environments/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/lifecycle_environments/update.html)  | Update an environment |
| environments_puppetclasses_environment_id_showpuppetclasses | [GET /api/environments/:environment_id/puppetclasses/:id](https://theforeman.org/api/1.16/apidoc/v2/puppetclasses/show.html)  | Show a Puppet class for an environment |
| environments_puppetclasses_index | [GET /api/environments/:environment_id/puppetclasses](https://theforeman.org/api/1.16/apidoc/v2/puppetclasses/index.html)  | List all Puppet classes for an environment |
| environments_repositories_nvironments | [GET /katello/api/environments/:environment_id/products/:product_id/repositories](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/index.html)  | List of repositories belonging to a product in an environment |
| environments_show | [GET /api/environments/:id](https://theforeman.org/api/1.16/apidoc/v2/environments/show.html)  | Show an environment |
| environments_smart_class_parameters_environment_id_indexpuppetclasses | [GET /api/environments/:environment_id/puppetclasses/:puppetclass_id/smart_class_parameters](https://theforeman.org/api/1.16/apidoc/v2/smart_class_parameters/index.html)  | List of smart class parameters for a specific environment/Puppet class combination |
| environments_smart_class_parameters_index | [GET /api/environments/:environment_id/smart_class_parameters](https://theforeman.org/api/1.16/apidoc/v2/smart_class_parameters/index.html)  | List of smart class parameters for a specific environment |
| environments_smart_proxies_environment_id_smart_import_puppetclassesproxies | [POST /api/environments/:environment_id/smart_proxies/:id/import_puppetclasses](https://theforeman.org/api/1.16/apidoc/v2/smart_proxies/import_puppetclasses.html)  | Import puppet classes from puppet Capsule for an environment |
| environments_systems_index | [GET /katello/api/environments/:environment_id/systems](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/systems/index.html)  | List content hosts in environment |
| environments_template_combinations_create | [POST /api/environments/:environment_id/template_combinations](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/create.html)  | Add a template combination |
| environments_template_combinations_environment_id_template_showcombinations | [GET /api/environments/:environment_id/template_combinations/:id](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/show.html)  | Show template combination |
| environments_template_combinations_environment_id_template_updatecombinations | [PUT /api/environments/:environment_id/template_combinations/:id](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/update.html)  | Update template combination |
| environments_template_combinations_index | [GET /api/environments/:environment_id/template_combinations](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/index.html)  | List template combination |
| environments_update | [PUT /api/environments/:id](https://theforeman.org/api/1.16/apidoc/v2/environments/update.html)  | Update an environment |
| errata_index | [GET /katello/api/errata](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/errata/index.html)  | List errata |
| errata_show | [GET /katello/api/errata/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/errata/show.html)  | Show an erratum |
| fact_values_index | [GET /api/fact_values](https://theforeman.org/api/1.16/apidoc/v2/fact_values/index.html)  | List all fact values |
| filters_create | [POST /api/filters](https://theforeman.org/api/1.16/apidoc/v2/filters/create.html)  | Create a filter |
| filters_destroy | [DELETE /api/filters/:id](https://theforeman.org/api/1.16/apidoc/v2/filters/destroy.html)  | Delete a filter |
| filters_index | [GET /api/filters](https://theforeman.org/api/1.16/apidoc/v2/filters/index.html)  | List all filters |
| filters_show | [GET /api/filters/:id](https://theforeman.org/api/1.16/apidoc/v2/filters/show.html)  | Show a filter |
| filters_update | [PUT /api/filters/:id](https://theforeman.org/api/1.16/apidoc/v2/filters/update.html)  | Update a filter |
| gpg_keys_content | [POST /katello/api/gpg_keys/:id/content](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/gpg_keys/content.html)  | Upload gpg key contents |
| gpg_keys_create | [POST /katello/api/gpg_keys](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/gpg_keys/create.html)  | Create a gpg key |
| gpg_keys_destroy | [DELETE /katello/api/gpg_keys/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/gpg_keys/destroy.html)  | Destroy a gpg key |
| gpg_keys_index | [GET /katello/api/gpg_keys](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/gpg_keys/index.html)  | List gpg keys |
| gpg_keys_show | [GET /katello/api/gpg_keys/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/gpg_keys/show.html)  | Show a gpg key |
| gpg_keys_update | [PUT /katello/api/gpg_keys/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/gpg_keys/update.html)  | Update a repository |
| host_collections_add_hosts | [PUT /katello/api/host_collections/:id/add_hosts](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/host_collections/add_hosts.html)  | Add host to the host collection |
| host_collections_copy | [POST /katello/api/host_collections/:id/copy](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/host_collections/copy.html)  | Make copy of a host collection |
| host_collections_create | [POST /katello/api/host_collections](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/host_collections/create.html)  | Create a host collection |
| host_collections_destroy | [DELETE /katello/api/host_collections/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/host_collections/destroy.html)  | Destroy a host collection |
| host_collections_index | [GET /katello/api/host_collections](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/host_collections/index.html)  | List host collections |
| host_collections_remove_hosts | [PUT /katello/api/host_collections/:id/remove_hosts](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/host_collections/remove_hosts.html)  | Remove hosts from the host collection |
| host_collections_show | [GET /katello/api/host_collections/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/host_collections/show.html)  | Show a host collection |
| host_collections_update | [PUT /katello/api/host_collections/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/host_collections/update.html)  | Update a host collection |
| hostgroups_clone | [POST /api/hostgroups/:id/clone](https://theforeman.org/api/1.16/apidoc/v2/hostgroups/clone.html)  | Clone a host group |
| hostgroups_create | [POST /api/hostgroups](https://theforeman.org/api/1.16/apidoc/v2/hostgroups/create.html)  | Create a host group |
| hostgroups_destroy | [DELETE /api/hostgroups/:id](https://theforeman.org/api/1.16/apidoc/v2/hostgroups/destroy.html)  | Delete a host group |
| hostgroups_hostgroup_classes_create | [POST /api/hostgroups/:hostgroup_id/puppetclass_ids](https://theforeman.org/api/1.16/apidoc/v2/hostgroup_classes/create.html)  | Add a Puppet class to host group |
| hostgroups_hostgroup_classes_hostgroup_id_puppetclass_destroyids | [DELETE /api/hostgroups/:hostgroup_id/puppetclass_ids/:id](https://theforeman.org/api/1.16/apidoc/v2/hostgroup_classes/destroy.html)  | Remove a Puppet class from host group |
| hostgroups_hostgroup_classes_index | [GET /api/hostgroups/:hostgroup_id/puppetclass_ids](https://theforeman.org/api/1.16/apidoc/v2/hostgroup_classes/index.html)  | List all Puppet class IDs for host group |
| hostgroups_hosts_index | [GET /api/hostgroups/:hostgroup_id/hosts](https://theforeman.org/api/1.16/apidoc/v2/hosts/index.html)  | List all hosts for a host group |
| hostgroups_index | [GET /api/hostgroups](https://theforeman.org/api/1.16/apidoc/v2/hostgroups/index.html)  | List all host groups |
| hostgroups_parameters_create | [POST /api/hostgroups/:hostgroup_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/create.html)  | Create a nested parameter for a host group |
| hostgroups_parameters_hostgroup_id_destroyparameters | [DELETE /api/hostgroups/:hostgroup_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/destroy.html)  | Delete a nested parameter for a host group |
| hostgroups_parameters_hostgroup_id_showparameters | [GET /api/hostgroups/:hostgroup_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/show.html)  | Show a nested parameter for a host group |
| hostgroups_parameters_hostgroup_id_updateparameters | [PUT /api/hostgroups/:hostgroup_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/update.html)  | Update a nested parameter for a host group |
| hostgroups_parameters_index | [GET /api/hostgroups/:hostgroup_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/index.html)  | List all parameters for a host group |
| hostgroups_parameters_reset | [DELETE /api/hostgroups/:hostgroup_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/reset.html)  | Delete all nested parameters for a host group |
| hostgroups_puppetclasses_hostgroup_id_showpuppetclasses | [GET /api/hostgroups/:hostgroup_id/puppetclasses/:id](https://theforeman.org/api/1.16/apidoc/v2/puppetclasses/show.html)  | Show a Puppet class for a host group |
| hostgroups_puppetclasses_index | [GET /api/hostgroups/:hostgroup_id/puppetclasses](https://theforeman.org/api/1.16/apidoc/v2/puppetclasses/index.html)  | List all Puppet classes for a host group |
| hostgroups_show | [GET /api/hostgroups/:id](https://theforeman.org/api/1.16/apidoc/v2/hostgroups/show.html)  | Show a host group |
| hostgroups_smart_class_parameters_index | [GET /api/hostgroups/:hostgroup_id/smart_class_parameters](https://theforeman.org/api/1.16/apidoc/v2/smart_class_parameters/index.html)  | List of smart class parameters for a specific host group |
| hostgroups_smart_variables_index | [GET /api/hostgroups/:hostgroup_id/smart_variables](https://theforeman.org/api/1.16/apidoc/v2/smart_variables/index.html)  | List of smart variables for a specific host group |
| hostgroups_template_combinations_create | [POST /api/hostgroups/:hostgroup_id/template_combinations](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/create.html)  | Add a template combination |
| hostgroups_template_combinations_hostgroup_id_template_showcombinations | [GET /api/hostgroups/:hostgroup_id/template_combinations/:id](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/show.html)  | Show template combination |
| hostgroups_template_combinations_hostgroup_id_template_updatecombinations | [PUT /api/hostgroups/:hostgroup_id/template_combinations/:id](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/update.html)  | Update template combination |
| hostgroups_template_combinations_index | [GET /api/hostgroups/:hostgroup_id/template_combinations](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/index.html)  | List template combination |
| hostgroups_update | [PUT /api/hostgroups/:id](https://theforeman.org/api/1.16/apidoc/v2/hostgroups/update.html)  | Update a host group |
| hosts_audits_index | [GET /api/hosts/:host_id/audits](https://theforeman.org/api/1.16/apidoc/v2/audits/index.html)  | List all audits for a given host |
| hosts_boot | [PUT /api/hosts/:id/boot](https://theforeman.org/api/1.16/apidoc/v2/hosts/boot.html)  | Boot host from specified device |
| hosts_config_reports_last | [GET /api/hosts/:host_id/config_reports/last](https://theforeman.org/api/1.16/apidoc/v2/config_reports/last.html)  | Show the last report for a host |
| hosts_create | [POST /api/hosts](https://theforeman.org/api/1.16/apidoc/v2/hosts/create.html)  | Create a host |
| hosts_destroy | [DELETE /api/hosts/:id](https://theforeman.org/api/1.16/apidoc/v2/hosts/destroy.html)  | Delete a host |
| hosts_disassociate | [PUT /api/hosts/:id/disassociate](https://theforeman.org/api/1.16/apidoc/v2/hosts/disassociate.html)  | Disassociate the host from a VM |
| hosts_enc | [GET /api/hosts/:id/enc](https://theforeman.org/api/1.16/apidoc/v2/hosts/enc.html)  | Get ENC values of host |
| hosts_fact_values_index | [GET /api/hosts/:host_id/facts](https://theforeman.org/api/1.16/apidoc/v2/fact_values/index.html)  | List all fact values of a given host |
| hosts_facts | [POST /api/hosts/facts](https://theforeman.org/api/1.16/apidoc/v2/hosts/facts.html)  | Upload facts for a host, creating the host if required |
| hosts_host_classes_create | [POST /api/hosts/:host_id/puppetclass_ids](https://theforeman.org/api/1.16/apidoc/v2/host_classes/create.html)  | Add a Puppet class to host |
| hosts_host_classes_host_id_puppetclass_destroyids | [DELETE /api/hosts/:host_id/puppetclass_ids/:id](https://theforeman.org/api/1.16/apidoc/v2/host_classes/destroy.html)  | Remove a Puppet class from host |
| hosts_host_classes_index | [GET /api/hosts/:host_id/puppetclass_ids](https://theforeman.org/api/1.16/apidoc/v2/host_classes/index.html)  | List all Puppet class IDs for host |
| hosts_host_collections | [PUT /api/hosts/:host_id/host_collections](https://theforeman.org/api/1.16/apidoc/v2/hosts/host_collections.html)  | Alter a hosts host collections |
| hosts_host_errata_apply | [PUT /api/hosts/:host_id/errata/apply](https://theforeman.org/api/1.16/apidoc/v2/host_errata/apply.html)  | Schedule errata for installation |
| hosts_host_errata_host_id_showerrata | [GET /api/hosts/:host_id/errata/:id](https://theforeman.org/api/1.16/apidoc/v2/host_errata/show.html)  | Retrieve a single errata for a host |
| hosts_host_errata_index | [GET /api/hosts/:host_id/errata](https://theforeman.org/api/1.16/apidoc/v2/host_errata/index.html)  | List errata available for the content host |
| hosts_host_packages_index | [GET /api/hosts/:host_id/packages](https://theforeman.org/api/1.16/apidoc/v2/host_packages/index.html)  | List packages installed on the host |
| hosts_host_packages_install | [PUT /api/hosts/:host_id/packages/install](https://theforeman.org/api/1.16/apidoc/v2/host_packages/install.html)  | Install packages remotely |
| hosts_host_packages_remove | [PUT /api/hosts/:host_id/packages/remove](https://theforeman.org/api/1.16/apidoc/v2/host_packages/remove.html)  | Uninstall packages remotely |
| hosts_host_packages_upgrade | [PUT /api/hosts/:host_id/packages/upgrade](https://theforeman.org/api/1.16/apidoc/v2/host_packages/upgrade.html)  | Update packages remotely |
| hosts_host_packages_upgrade_all | [PUT /api/hosts/:host_id/packages/upgrade_all](https://theforeman.org/api/1.16/apidoc/v2/host_packages/upgrade_all.html)  | Update packages remotely |
| hosts_host_subscriptions_add_subscriptions | [PUT /api/hosts/:host_id/subscriptions/add_subscriptions](https://theforeman.org/api/1.16/apidoc/v2/host_subscriptions/add_subscriptions.html)  | Add a subscription to a host |
| hosts_host_subscriptions_auto_attach | [PUT /api/hosts/:host_id/subscriptions/auto_attach](https://theforeman.org/api/1.16/apidoc/v2/host_subscriptions/auto_attach.html)  | Trigger an auto-attach of subscriptions |
| hosts_host_subscriptions_content_override | [PUT /api/hosts/:host_id/subscriptions/content_override](https://theforeman.org/api/1.16/apidoc/v2/host_subscriptions/content_override.html)  | Set content overrides for the host |
| hosts_host_subscriptions_create | [POST /api/hosts/subscriptions](https://theforeman.org/api/1.16/apidoc/v2/host_subscriptions/create.html)  | Register a host with subscription and information. |
| hosts_host_subscriptions_destroy | [DELETE /api/hosts/:host_id/subscriptions](https://theforeman.org/api/1.16/apidoc/v2/host_subscriptions/destroy.html)  | Unregister the host as a subscription consumer |
| hosts_host_subscriptions_events | [GET /api/hosts/:host_id/subscriptions/events](https://theforeman.org/api/1.16/apidoc/v2/host_subscriptions/events.html)  | List subscription events for the host |
| hosts_host_subscriptions_index | [GET /api/hosts/:host_id/subscriptions](https://theforeman.org/api/1.16/apidoc/v2/host_subscriptions/index.html)  | List a host's subscriptions |
| hosts_host_subscriptions_product_content | [GET /api/hosts/:host_id/subscriptions/product_content](https://theforeman.org/api/1.16/apidoc/v2/host_subscriptions/product_content.html)  | Get content and overrides for the host |
| hosts_host_subscriptions_remove_subscriptions | [PUT /api/hosts/:host_id/subscriptions/remove_subscriptions](https://theforeman.org/api/1.16/apidoc/v2/host_subscriptions/remove_subscriptions.html)  |  |
| hosts_hosts_bulk_actions_add_subscriptions | [PUT /api/hosts/bulk/subscriptions/add_subscriptions](https://theforeman.org/api/1.16/apidoc/v2/hosts_bulk_actions/add_subscriptions.html)  | Add subscriptions to one or more hosts |
| hosts_hosts_bulk_actions_auto_attach | [PUT /api/hosts/bulk/subscriptions/auto_attach](https://theforeman.org/api/1.16/apidoc/v2/hosts_bulk_actions/auto_attach.html)  | Trigger an auto-attach of subscriptions on one or more hosts |
| hosts_hosts_bulk_actions_available_incremental_updates | [POST /api/hosts/bulk/available_incremental_updates](https://theforeman.org/api/1.16/apidoc/v2/hosts_bulk_actions/available_incremental_updates.html)  | Given a set of hosts and errata, lists the content view versions and environments that need updating. |
| hosts_hosts_bulk_actions_bulk_add_host_collections | [PUT /api/hosts/bulk/add_host_collections](https://theforeman.org/api/1.16/apidoc/v2/hosts_bulk_actions/bulk_add_host_collections.html)  | Add one or more host collections to one or more hosts |
| hosts_hosts_bulk_actions_bulk_remove_host_collections | [PUT /api/hosts/bulk/remove_host_collections](https://theforeman.org/api/1.16/apidoc/v2/hosts_bulk_actions/bulk_remove_host_collections.html)  | Remove one or more host collections from one or more hosts |
| hosts_hosts_bulk_actions_destroy_hosts | [PUT /api/hosts/bulk/destroy](https://theforeman.org/api/1.16/apidoc/v2/hosts_bulk_actions/destroy_hosts.html)  | Destroy one or more hosts |
| hosts_hosts_bulk_actions_environment_content_view | [PUT /api/hosts/bulk/environment_content_view](https://theforeman.org/api/1.16/apidoc/v2/hosts_bulk_actions/environment_content_view.html)  | Assign the environment and content view to one or more hosts |
| hosts_hosts_bulk_actions_install_content | [PUT /api/hosts/bulk/install_content](https://theforeman.org/api/1.16/apidoc/v2/hosts_bulk_actions/install_content.html)  | Install content on one or more hosts |
| hosts_hosts_bulk_actions_installable_errata | [POST /api/hosts/bulk/applicable_errata](https://theforeman.org/api/1.16/apidoc/v2/hosts_bulk_actions/installable_errata.html)  | Fetch applicable errata for a system. |
| hosts_hosts_bulk_actions_remove_content | [PUT /api/hosts/bulk/remove_content](https://theforeman.org/api/1.16/apidoc/v2/hosts_bulk_actions/remove_content.html)  | Remove content on one or more hosts |
| hosts_hosts_bulk_actions_remove_subscriptions | [PUT /api/hosts/bulk/subscriptions/remove_subscriptions](https://theforeman.org/api/1.16/apidoc/v2/hosts_bulk_actions/remove_subscriptions.html)  | Remove subscriptions from one or more hosts |
| hosts_hosts_bulk_actions_update_content | [PUT /api/hosts/bulk/update_content](https://theforeman.org/api/1.16/apidoc/v2/hosts_bulk_actions/update_content.html)  | Update content on one or more hosts |
| hosts_id_get_statusstatus | [GET /api/hosts/:id/status/:type](https://theforeman.org/api/1.16/apidoc/v2/hosts/get_status.html)  | Get status of host |
| hosts_id_templatetemplate | [GET /api/hosts/:id/template/:kind](https://theforeman.org/api/1.16/apidoc/v2/hosts/template.html)  | Preview rendered provisioning template content |
| hosts_index | [GET /api/hosts](https://theforeman.org/api/1.16/apidoc/v2/hosts/index.html)  | List all hosts |
| hosts_interfaces_create | [POST /api/hosts/:host_id/interfaces](https://theforeman.org/api/1.16/apidoc/v2/interfaces/create.html)  | Create an interface on a host |
| hosts_interfaces_host_id_destroyinterfaces | [DELETE /api/hosts/:host_id/interfaces/:id](https://theforeman.org/api/1.16/apidoc/v2/interfaces/destroy.html)  | Delete a host's interface |
| hosts_interfaces_host_id_showinterfaces | [GET /api/hosts/:host_id/interfaces/:id](https://theforeman.org/api/1.16/apidoc/v2/interfaces/show.html)  | Show an interface for host |
| hosts_interfaces_host_id_updateinterfaces | [PUT /api/hosts/:host_id/interfaces/:id](https://theforeman.org/api/1.16/apidoc/v2/interfaces/update.html)  | Update a host's interface |
| hosts_interfaces_index | [GET /api/hosts/:host_id/interfaces](https://theforeman.org/api/1.16/apidoc/v2/interfaces/index.html)  | List all interfaces for host |
| hosts_parameters_create | [POST /api/hosts/:host_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/create.html)  | Create a nested parameter for a host |
| hosts_parameters_host_id_destroyparameters | [DELETE /api/hosts/:host_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/destroy.html)  | Delete a nested parameter for a host |
| hosts_parameters_host_id_showparameters | [GET /api/hosts/:host_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/show.html)  | Show a nested parameter for a host |
| hosts_parameters_host_id_updateparameters | [PUT /api/hosts/:host_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/update.html)  | Update a nested parameter for a host |
| hosts_parameters_index | [GET /api/hosts/:host_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/index.html)  | List all parameters for a host |
| hosts_parameters_reset | [DELETE /api/hosts/:host_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/reset.html)  | Delete all nested parameters for a host |
| hosts_power | [PUT /api/hosts/:id/power](https://theforeman.org/api/1.16/apidoc/v2/hosts/power.html)  | Run a power operation on host |
| hosts_puppetclasses_host_id_showpuppetclasses | [GET /api/hosts/:host_id/puppetclasses/:id](https://theforeman.org/api/1.16/apidoc/v2/puppetclasses/show.html)  | Show a Puppet class for host |
| hosts_puppetclasses_index | [GET /api/hosts/:host_id/puppetclasses](https://theforeman.org/api/1.16/apidoc/v2/puppetclasses/index.html)  | List all Puppet classes for a host |
| hosts_puppetrun | [PUT /api/hosts/:id/puppetrun](https://theforeman.org/api/1.16/apidoc/v2/hosts/puppetrun.html)  | Force a Puppet agent run on the host |
| hosts_rebuild_config | [PUT /api/hosts/:id/rebuild_config](https://theforeman.org/api/1.16/apidoc/v2/hosts/rebuild_config.html)  | Rebuild orchestration config |
| hosts_reports_last | [GET /api/hosts/:host_id/reports/last](https://theforeman.org/api/1.16/apidoc/v2/reports/last.html)  | Show the last report for a host |
| hosts_show | [GET /api/hosts/:id](https://theforeman.org/api/1.16/apidoc/v2/hosts/show.html)  | Show a host |
| hosts_smart_class_parameters_index | [GET /api/hosts/:host_id/smart_class_parameters](https://theforeman.org/api/1.16/apidoc/v2/smart_class_parameters/index.html)  | List of smart class parameters for a specific host |
| hosts_smart_variables_index | [GET /api/hosts/:host_id/smart_variables](https://theforeman.org/api/1.16/apidoc/v2/smart_variables/index.html)  | List of smart variables for a specific host |
| hosts_status | [GET /api/hosts/:id/status](https://theforeman.org/api/1.16/apidoc/v2/hosts/status.html)  | Get configuration status of host |
| hosts_update | [PUT /api/hosts/:id](https://theforeman.org/api/1.16/apidoc/v2/hosts/update.html)  | Update a host |
| hosts_vm_compute_attributes | [GET /api/hosts/:id/vm_compute_attributes](https://theforeman.org/api/1.16/apidoc/v2/hosts/vm_compute_attributes.html)  | Get vm attributes of host |
| job_invocations_create | [POST /api/job_invocations](https://theforeman.org/api/1.16/apidoc/v2/job_invocations/create.html)  | Create a job invocation |
| job_invocations_id_outputhosts | [GET /api/job_invocations/:id/hosts/:host_id](https://theforeman.org/api/1.16/apidoc/v2/job_invocations/output.html)  | Get output for a host |
| job_invocations_index | [GET /api/job_invocations](https://theforeman.org/api/1.16/apidoc/v2/job_invocations/index.html)  | List job invocations |
| job_invocations_show | [GET /api/job_invocations/:id](https://theforeman.org/api/1.16/apidoc/v2/job_invocations/show.html)  | Show job invocation |
| job_templates_clone | [POST /api/job_templates/:id/clone](https://theforeman.org/api/1.16/apidoc/v2/job_templates/clone.html)  | Clone a provision template |
| job_templates_create | [POST /api/job_templates](https://theforeman.org/api/1.16/apidoc/v2/job_templates/create.html)  | Create a job template |
| job_templates_destroy | [DELETE /api/job_templates/:id](https://theforeman.org/api/1.16/apidoc/v2/job_templates/destroy.html)  | Delete a job template |
| job_templates_export | [GET /api/job_templates/:id/export](https://theforeman.org/api/1.16/apidoc/v2/job_templates/export.html)  | Export a job template to ERB |
| job_templates_import_ | [POST /api/job_templates/import](https://theforeman.org/api/1.16/apidoc/v2/job_templates/import.html)  | Import a job template from ERB |
| job_templates_index | [GET /api/job_templates](https://theforeman.org/api/1.16/apidoc/v2/job_templates/index.html)  | List job templates |
| job_templates_revision | [GET /api/job_templates/revision](https://theforeman.org/api/1.16/apidoc/v2/job_templates/revision.html)  |  |
| job_templates_show | [GET /api/job_templates/:id](https://theforeman.org/api/1.16/apidoc/v2/job_templates/show.html)  | Show job template details |
| job_templates_update | [PUT /api/job_templates/:id](https://theforeman.org/api/1.16/apidoc/v2/job_templates/update.html)  | Update a job template |
| locations_auth_source_ldaps_index | [GET /api/locations/:location_id/auth_source_ldaps](https://theforeman.org/api/1.16/apidoc/v2/auth_source_ldaps/index.html)  | List LDAP authentication sources per location |
| locations_config_templates_index | [GET /api/locations/:location_id/config_templates](https://theforeman.org/api/1.16/apidoc/v2/config_templates/index.html)  | List provisioning templates per location |
| locations_create | [POST /api/locations](https://theforeman.org/api/1.16/apidoc/v2/locations/create.html)  | Create a location |
| locations_destroy | [DELETE /api/locations/:id](https://theforeman.org/api/1.16/apidoc/v2/locations/destroy.html)  | Delete a location |
| locations_domains_index | [GET /api/locations/:location_id/domains](https://theforeman.org/api/1.16/apidoc/v2/domains/index.html)  | List of domains per location |
| locations_environments_index | [GET /api/locations/:location_id/environments](https://theforeman.org/api/1.16/apidoc/v2/environments/index.html)  | List environments per location |
| locations_hostgroups_index | [GET /api/locations/:location_id/hostgroups](https://theforeman.org/api/1.16/apidoc/v2/hostgroups/index.html)  | List all host groups per location |
| locations_hosts_index | [GET /api/locations/:location_id/hosts](https://theforeman.org/api/1.16/apidoc/v2/hosts/index.html)  | List hosts per location |
| locations_index | [GET /api/locations](https://theforeman.org/api/1.16/apidoc/v2/locations/index.html)  | List all locations |
| locations_job_templates_index | [GET /api/locations/:location_id/job_templates](https://theforeman.org/api/1.16/apidoc/v2/job_templates/index.html)  | List job templates per location |
| locations_media_index | [GET /api/locations/:location_id/media](https://theforeman.org/api/1.16/apidoc/v2/media/index.html)  | List all media per location |
| locations_parameters_create | [POST /api/locations/:location_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/create.html)  | Create a nested parameter for a location |
| locations_parameters_index | [GET /api/locations/:location_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/index.html)  | List all parameters for a location |
| locations_parameters_location_id_destroyparameters | [DELETE /api/locations/:location_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/destroy.html)  | Delete a nested parameter for a location |
| locations_parameters_location_id_showparameters | [GET /api/locations/:location_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/show.html)  | Show a nested parameter for a location |
| locations_parameters_location_id_updateparameters | [PUT /api/locations/:location_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/update.html)  | Update a nested parameter for a location |
| locations_parameters_reset | [DELETE /api/locations/:location_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/reset.html)  | Delete all nested parameter for a location |
| locations_provisioning_templates_index | [GET /api/locations/:location_id/provisioning_templates](https://theforeman.org/api/1.16/apidoc/v2/provisioning_templates/index.html)  | List provisioning templates per location |
| locations_ptables_index | [GET /api/locations/:location_id/ptables](https://theforeman.org/api/1.16/apidoc/v2/ptables/index.html)  | List all partition tables per location |
| locations_show | [GET /api/locations/:id](https://theforeman.org/api/1.16/apidoc/v2/locations/show.html)  | Show a location |
| locations_subnets_index | [GET /api/locations/:location_id/subnets](https://theforeman.org/api/1.16/apidoc/v2/subnets/index.html)  | List of subnets per location |
| locations_update | [PUT /api/locations/:id](https://theforeman.org/api/1.16/apidoc/v2/locations/update.html)  | Update a location |
| locations_users_index | [GET /api/locations/:location_id/users](https://theforeman.org/api/1.16/apidoc/v2/users/index.html)  | List all users for location |
| mail_notifications_index | [GET /api/mail_notifications](https://theforeman.org/api/1.16/apidoc/v2/mail_notifications/index.html)  | List of email notifications |
| mail_notifications_show | [GET /api/mail_notifications/:id](https://theforeman.org/api/1.16/apidoc/v2/mail_notifications/show.html)  | Show an email notification |
| media_create | [POST /api/media](https://theforeman.org/api/1.16/apidoc/v2/media/create.html)  | Create a medium |
| media_destroy | [DELETE /api/media/:id](https://theforeman.org/api/1.16/apidoc/v2/media/destroy.html)  | Delete a medium |
| media_index | [GET /api/media](https://theforeman.org/api/1.16/apidoc/v2/media/index.html)  | List all installation media |
| media_operatingsystems_index | [GET /api/media/:medium_id/operatingsystems](https://theforeman.org/api/1.16/apidoc/v2/operatingsystems/index.html)  | List all operating systems for nested medium |
| media_show | [GET /api/media/:id](https://theforeman.org/api/1.16/apidoc/v2/media/show.html)  | Show a medium |
| media_update | [PUT /api/media/:id](https://theforeman.org/api/1.16/apidoc/v2/media/update.html)  | Update a medium |
| models_create | [POST /api/models](https://theforeman.org/api/1.16/apidoc/v2/models/create.html)  | Create a hardware model |
| models_destroy | [DELETE /api/models/:id](https://theforeman.org/api/1.16/apidoc/v2/models/destroy.html)  | Delete a hardware model |
| models_index | [GET /api/models](https://theforeman.org/api/1.16/apidoc/v2/models/index.html)  | List all hardware models |
| models_show | [GET /api/models/:id](https://theforeman.org/api/1.16/apidoc/v2/models/show.html)  | Show a hardware model |
| models_update | [PUT /api/models/:id](https://theforeman.org/api/1.16/apidoc/v2/models/update.html)  | Update a hardware model |
| operatingsystems_architectures_index | [GET /api/operatingsystems/:operatingsystem_id/architectures](https://theforeman.org/api/1.16/apidoc/v2/architectures/index.html)  | List all architectures for operating system |
| operatingsystems_bootfiles | [GET /api/operatingsystems/:id/bootfiles](https://theforeman.org/api/1.16/apidoc/v2/operatingsystems/bootfiles.html)  | List boot files for an operating system |
| operatingsystems_config_templates_index | [GET /api/operatingsystems/:operatingsystem_id/config_templates](https://theforeman.org/api/1.16/apidoc/v2/config_templates/index.html)  | List provisioning templates per operating system |
| operatingsystems_create | [POST /api/operatingsystems](https://theforeman.org/api/1.16/apidoc/v2/operatingsystems/create.html)  | Create an operating system |
| operatingsystems_destroy | [DELETE /api/operatingsystems/:id](https://theforeman.org/api/1.16/apidoc/v2/operatingsystems/destroy.html)  | Delete an operating system |
| operatingsystems_images_index | [GET /api/operatingsystems/:operatingsystem_id/images](https://theforeman.org/api/1.16/apidoc/v2/images/index.html)  | List all images for operating system |
| operatingsystems_images_operatingsystem_id_showimages | [GET /api/operatingsystems/:operatingsystem_id/images/:id](https://theforeman.org/api/1.16/apidoc/v2/images/show.html)  | Show an image |
| operatingsystems_index | [GET /api/operatingsystems](https://theforeman.org/api/1.16/apidoc/v2/operatingsystems/index.html)  | List all operating systems |
| operatingsystems_media_index | [GET /api/operatingsystems/:operatingsystem_id/media](https://theforeman.org/api/1.16/apidoc/v2/media/index.html)  | List all media for an operating system |
| operatingsystems_os_default_templates_create | [POST /api/operatingsystems/:operatingsystem_id/os_default_templates](https://theforeman.org/api/1.16/apidoc/v2/os_default_templates/create.html)  | Create a default template combination for an operating system |
| operatingsystems_os_default_templates_index | [GET /api/operatingsystems/:operatingsystem_id/os_default_templates](https://theforeman.org/api/1.16/apidoc/v2/os_default_templates/index.html)  | List default templates combinations for an operating system |
| operatingsystems_os_default_templates_operatingsystem_id_os_default_destroytemplates | [DELETE /api/operatingsystems/:operatingsystem_id/os_default_templates/:id](https://theforeman.org/api/1.16/apidoc/v2/os_default_templates/destroy.html)  | Delete a default template combination for an operating system |
| operatingsystems_os_default_templates_operatingsystem_id_os_default_showtemplates | [GET /api/operatingsystems/:operatingsystem_id/os_default_templates/:id](https://theforeman.org/api/1.16/apidoc/v2/os_default_templates/show.html)  | Show a default template combination for an operating system |
| operatingsystems_os_default_templates_operatingsystem_id_os_default_updatetemplates | [PUT /api/operatingsystems/:operatingsystem_id/os_default_templates/:id](https://theforeman.org/api/1.16/apidoc/v2/os_default_templates/update.html)  | Update a default template combination for an operating system |
| operatingsystems_parameters_create | [POST /api/operatingsystems/:operatingsystem_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/create.html)  | Create a nested parameter for an operating system |
| operatingsystems_parameters_index | [GET /api/operatingsystems/:operatingsystem_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/index.html)  | List all parameters for an operating system |
| operatingsystems_parameters_operatingsystem_id_destroyparameters | [DELETE /api/operatingsystems/:operatingsystem_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/destroy.html)  | Delete a nested parameter for an operating system |
| operatingsystems_parameters_operatingsystem_id_showparameters | [GET /api/operatingsystems/:operatingsystem_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/show.html)  | Show a nested parameter for an operating system |
| operatingsystems_parameters_operatingsystem_id_updateparameters | [PUT /api/operatingsystems/:operatingsystem_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/update.html)  | Update a nested parameter for an operating system |
| operatingsystems_parameters_reset | [DELETE /api/operatingsystems/:operatingsystem_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/reset.html)  | Delete all nested parameters for an operating system |
| operatingsystems_provisioning_templates_index | [GET /api/operatingsystems/:operatingsystem_id/provisioning_templates](https://theforeman.org/api/1.16/apidoc/v2/provisioning_templates/index.html)  | List provisioning templates per operating system |
| operatingsystems_ptables_index | [GET /api/operatingsystems/:operatingsystem_id/ptables](https://theforeman.org/api/1.16/apidoc/v2/ptables/index.html)  | List all partition tables for an operating system |
| operatingsystems_show | [GET /api/operatingsystems/:id](https://theforeman.org/api/1.16/apidoc/v2/operatingsystems/show.html)  | Show an operating system |
| operatingsystems_update | [PUT /api/operatingsystems/:id](https://theforeman.org/api/1.16/apidoc/v2/operatingsystems/update.html)  | Update an operating system |
| orchestration_tasks_index | [GET /api/orchestration/:id/tasks](https://theforeman.org/api/1.16/apidoc/v2/tasks/index.html)  | List all tasks for a given orchestration event |
| organizations_activation_keys_index | [GET /katello/api/organizations/:organization_id/activation_keys](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/activation_keys/index.html)  |  |
| organizations_auth_source_ldaps_index | [GET /api/organizations/:organization_id/auth_source_ldaps](https://theforeman.org/api/1.16/apidoc/v2/auth_source_ldaps/index.html)  | List LDAP authentication sources per organization |
| organizations_autoattach_subscriptions | [POST /katello/api/organizations/:id/autoattach_subscriptions](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/organizations/autoattach_subscriptions.html)  | Auto-attach available subscriptions to all hosts within an organization. Asynchronous operation. |
| organizations_cancel_repo_discover | [PUT /katello/api/organizations/:label/cancel_repo_discover](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/organizations/cancel_repo_discover.html)  | Cancel repository discovery |
| organizations_config_templates_index | [GET /api/organizations/:organization_id/config_templates](https://theforeman.org/api/1.16/apidoc/v2/config_templates/index.html)  | List provisioning templates per organization |
| organizations_content_views_create | [POST /katello/api/organizations/:organization_id/content_views](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_views/create.html)  | Create a content view |
| organizations_content_views_index | [GET /katello/api/organizations/:organization_id/content_views](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_views/index.html)  | List content views |
| organizations_create | [POST /katello/api/organizations](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/organizations/create.html)  | Create organization |
| organizations_destroy | [DELETE /katello/api/organizations/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/organizations/destroy.html)  | Delete an organization |
| organizations_domains_index | [GET /api/organizations/:organization_id/domains](https://theforeman.org/api/1.16/apidoc/v2/domains/index.html)  | List of domains per organization |
| organizations_download_debug_certificate | [GET /katello/api/organizations/:label/download_debug_certificate](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/organizations/download_debug_certificate.html)  | Download a debug certificate |
| organizations_environments_index | [GET /api/organizations/:organization_id/environments](https://theforeman.org/api/1.16/apidoc/v2/environments/index.html)  | List environments per organization |
| organizations_host_collections_create | [POST /katello/api/organizations/:organization_id/host_collections](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/host_collections/create.html)  | Create a host collection |
| organizations_host_collections_index | [GET /katello/api/organizations/:organization_id/host_collections](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/host_collections/index.html)  | List host collections within an organization |
| organizations_hostgroups_index | [GET /api/organizations/:organization_id/hostgroups](https://theforeman.org/api/1.16/apidoc/v2/hostgroups/index.html)  | List all host groups per organization |
| organizations_hosts_index | [GET /api/organizations/:organization_id/hosts](https://theforeman.org/api/1.16/apidoc/v2/hosts/index.html)  | List hosts per organization |
| organizations_index | [GET /katello/api/organizations](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/organizations/index.html)  | List all organizations |
| organizations_job_templates_index | [GET /api/organizations/:organization_id/job_templates](https://theforeman.org/api/1.16/apidoc/v2/job_templates/index.html)  | List job templates per organization |
| organizations_lifecycle_environments_create | [POST /katello/api/organizations/:organization_id/environments](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/lifecycle_environments/create.html)  | Create an environment in an organization |
| organizations_lifecycle_environments_index | [GET /katello/api/organizations/:organization_id/environments](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/lifecycle_environments/index.html)  | List environments in an organization |
| organizations_lifecycle_environments_paths | [GET /katello/api/organizations/:organization_id/environments/paths](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/lifecycle_environments/paths.html)  | List environment paths |
| organizations_lifecycle_environments_rganizations | [GET /katello/api/organizations/:organization_id/environments/:environment_id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/lifecycle_environments/show.html)  | Show an environment |
| organizations_media_index | [GET /api/organizations/:organization_id/media](https://theforeman.org/api/1.16/apidoc/v2/media/index.html)  | List all media per organization |
| organizations_parameters_create | [POST /api/organizations/:organization_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/create.html)  | Create a nested parameter for an organization |
| organizations_parameters_index | [GET /api/organizations/:organization_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/index.html)  | List all parameters for an organization |
| organizations_parameters_organization_id_destroyparameters | [DELETE /api/organizations/:organization_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/destroy.html)  | Delete a nested parameter for an organization |
| organizations_parameters_organization_id_showparameters | [GET /api/organizations/:organization_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/show.html)  | Show a nested parameter for an organization |
| organizations_parameters_organization_id_updateparameters | [PUT /api/organizations/:organization_id/parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/parameters/update.html)  | Update a nested parameter for an organization |
| organizations_parameters_reset | [DELETE /api/organizations/:organization_id/parameters](https://theforeman.org/api/1.16/apidoc/v2/parameters/reset.html)  | Delete all nested parameter for an organization |
| organizations_products_index | [GET /katello/api/organizations/:organization_id/products](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/products/index.html)  | List of products in an organization |
| organizations_products_rganizations | [GET /katello/api/organizations/:organization_id/sync_plans/:sync_plan_id/products](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/products/index.html)  | List of Products for sync plan |
| organizations_provisioning_templates_index | [GET /api/organizations/:organization_id/provisioning_templates](https://theforeman.org/api/1.16/apidoc/v2/provisioning_templates/index.html)  | List provisioning templates per organization |
| organizations_ptables_index | [GET /api/organizations/:organization_id/ptables](https://theforeman.org/api/1.16/apidoc/v2/ptables/index.html)  | List all partition tables per organization |
| organizations_redhat_provider | [GET /katello/api/organizations/:id/redhat_provider](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/organizations/redhat_provider.html)  | List all :resource_id |
| organizations_repo_discover | [PUT /katello/api/organizations/:id/repo_discover](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/organizations/repo_discover.html)  | Discover Repositories |
| organizations_repositories_rganizations | [GET /katello/api/organizations/:organization_id/environments/:environment_id/repositories](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/index.html)  | List repositories in the environment |
| organizations_show | [GET /katello/api/organizations/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/organizations/show.html)  | Show organization |
| organizations_subnets_index | [GET /api/organizations/:organization_id/subnets](https://theforeman.org/api/1.16/apidoc/v2/subnets/index.html)  | List of subnets per organization |
| organizations_subscriptions_delete_manifest | [POST /katello/api/organizations/:organization_id/subscriptions/delete_manifest](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/subscriptions/delete_manifest.html)  | Delete manifest from Red Hat provider |
| organizations_subscriptions_index | [GET /katello/api/organizations/:organization_id/subscriptions](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/subscriptions/index.html)  | List organization subscriptions |
| organizations_subscriptions_manifest_history | [GET /katello/api/organizations/:organization_id/subscriptions/manifest_history](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/subscriptions/manifest_history.html)  | obtain manifest history for subscriptions |
| organizations_subscriptions_refresh_manifest | [PUT /katello/api/organizations/:organization_id/subscriptions/refresh_manifest](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/subscriptions/refresh_manifest.html)  | Refresh previously imported manifest for Red Hat provider |
| organizations_subscriptions_rganizations | [GET /katello/api/organizations/:organization_id/subscriptions/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/subscriptions/show.html)  | Show a subscription |
| organizations_subscriptions_upload | [POST /katello/api/organizations/:organization_id/subscriptions/upload](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/subscriptions/upload.html)  | Upload a subscription manifest |
| organizations_sync_plans_create | [POST /katello/api/organizations/:organization_id/sync_plans](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/sync_plans/create.html)  | Create a sync plan |
| organizations_sync_plans_index | [GET /katello/api/organizations/:organization_id/sync_plans](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/sync_plans/index.html)  |  |
| organizations_sync_plans_rganizations | [GET /katello/api/organizations/:organization_id/sync_plans/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/sync_plans/show.html)  | Show a sync plan |
| organizations_sync_rganizations | [GET /katello/api/organizations/:organization_id/products/:product_id/sync](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/sync/index.html)  | Get status of repo synchronisation for given product |
| organizations_systems_index | [GET /katello/api/organizations/:organization_id/systems](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/systems/index.html)  | List content hosts in an organization |
| organizations_uebercerts_show | [GET /katello/api/organizations/:organization_id/uebercert](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/uebercerts/show.html)  | Show an ueber certificate for an organization |
| organizations_update | [PUT /katello/api/organizations/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/organizations/update.html)  | Update organization |
| organizations_users_index | [GET /api/organizations/:organization_id/users](https://theforeman.org/api/1.16/apidoc/v2/users/index.html)  | List all users for organization |
| ostree_branches_index | [GET /katello/api/ostree_branches](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/ostree_branches/index.html)  | List ostree_branches |
| ostree_branches_show | [GET /katello/api/ostree_branches/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/ostree_branches/show.html)  | Show an ostree branch |
| package_groups_index | [GET /katello/api/package_groups](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/package_groups/index.html)  | List package_groups |
| package_groups_show | [GET /katello/api/package_groups/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/package_groups/show.html)  | Show a package group |
| packages_index | [GET /katello/api/packages](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/packages/index.html)  | List packages |
| packages_show | [GET /katello/api/packages/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/packages/show.html)  | Show a package |
| permissions_index | [GET /api/permissions](https://theforeman.org/api/1.16/apidoc/v2/permissions/index.html)  | List all permissions |
| permissions_resource_types | [GET /api/permissions/resource_types](https://theforeman.org/api/1.16/apidoc/v2/permissions/resource_types.html)  | List available resource types. |
| permissions_show | [GET /api/permissions/:id](https://theforeman.org/api/1.16/apidoc/v2/permissions/show.html)  | Show a permission |
| ping_index | [GET /katello/api/ping](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/ping/index.html)  | Shows status of system and it's subcomponents |
| products_create | [POST /katello/api/products](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/products/create.html)  | Create a product |
| products_destroy | [DELETE /katello/api/products/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/products/destroy.html)  | Destroy a product |
| products_index | [GET /katello/api/products](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/products/index.html)  | List products |
| products_products_bulk_actions_destroy_products | [PUT /katello/api/products/bulk/destroy](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/products_bulk_actions/destroy_products.html)  | Destroy one or more products |
| products_products_bulk_actions_sync_products | [PUT /katello/api/products/bulk/sync](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/products_bulk_actions/sync_products.html)  | Sync one or more products |
| products_products_bulk_actions_update_sync_plans | [PUT /katello/api/products/bulk/sync_plan](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/products_bulk_actions/update_sync_plans.html)  | Sync one or more products |
| products_repositories_index | [GET /katello/api/products/:product_id/repositories](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/index.html)  | List of repositories for a product |
| products_repository_sets_index | [GET /katello/api/products/:product_id/repository_sets](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repository_sets/index.html)  | List repository sets for a product. |
| products_repository_sets_roducts | [GET /katello/api/products/:product_id/repository_sets/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repository_sets/show.html)  | Get info about a repository set |
| products_show | [GET /katello/api/products/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/products/show.html)  | Show a product |
| products_sync | [POST /katello/api/products/:id/sync](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/products/sync.html)  | Sync all repositories for a product |
| products_update | [PUT /katello/api/products/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/products/update.html)  | Updates a product |
| provisioning_templates_build_pxe_default | [POST /api/provisioning_templates/build_pxe_default](https://theforeman.org/api/1.16/apidoc/v2/provisioning_templates/build_pxe_default.html)  | Update the default PXE menu on all configured TFTP servers |
| provisioning_templates_clone | [POST /api/provisioning_templates/:id/clone](https://theforeman.org/api/1.16/apidoc/v2/provisioning_templates/clone.html)  | Clone a provision template |
| provisioning_templates_create | [POST /api/provisioning_templates](https://theforeman.org/api/1.16/apidoc/v2/provisioning_templates/create.html)  | Create a provisioning template |
| provisioning_templates_destroy | [DELETE /api/provisioning_templates/:id](https://theforeman.org/api/1.16/apidoc/v2/provisioning_templates/destroy.html)  | Delete a provisioning template |
| provisioning_templates_index | [GET /api/provisioning_templates](https://theforeman.org/api/1.16/apidoc/v2/provisioning_templates/index.html)  | List provisioning templates |
| provisioning_templates_operatingsystems_index | [GET /api/provisioning_templates/:provisioning_template_id/operatingsystems](https://theforeman.org/api/1.16/apidoc/v2/operatingsystems/index.html)  | List all operating systems for nested provisioning template |
| provisioning_templates_os_default_templates_index | [GET /api/provisioning_templates/:provisioning_template_id/os_default_templates](https://theforeman.org/api/1.16/apidoc/v2/os_default_templates/index.html)  | List operating systems where this template is set as a default |
| provisioning_templates_revision | [GET /api/provisioning_templates/revision](https://theforeman.org/api/1.16/apidoc/v2/provisioning_templates/revision.html)  |  |
| provisioning_templates_show | [GET /api/provisioning_templates/:id](https://theforeman.org/api/1.16/apidoc/v2/provisioning_templates/show.html)  | Show provisioning template details |
| provisioning_templates_template_combinations_create | [POST /api/provisioning_templates/:provisioning_template_id/template_combinations](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/create.html)  | Add a template combination |
| provisioning_templates_template_combinations_index | [GET /api/provisioning_templates/:provisioning_template_id/template_combinations](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/index.html)  | List template combination |
| provisioning_templates_template_combinations_provisioning_template_id_template_showcombinations | [GET /api/provisioning_templates/:provisioning_template_id/template_combinations/:id](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/show.html)  | Show template combination |
| provisioning_templates_template_combinations_provisioning_template_id_template_updatecombinations | [PUT /api/provisioning_templates/:provisioning_template_id/template_combinations/:id](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/update.html)  | Update template combination |
| provisioning_templates_update | [PUT /api/provisioning_templates/:id](https://theforeman.org/api/1.16/apidoc/v2/provisioning_templates/update.html)  | Update a provisioning template |
| ptables_clone | [POST /api/ptables/:id/clone](https://theforeman.org/api/1.16/apidoc/v2/ptables/clone.html)  | Clone a template |
| ptables_create | [POST /api/ptables](https://theforeman.org/api/1.16/apidoc/v2/ptables/create.html)  | Create a partition table |
| ptables_destroy | [DELETE /api/ptables/:id](https://theforeman.org/api/1.16/apidoc/v2/ptables/destroy.html)  | Delete a partition table |
| ptables_index | [GET /api/ptables](https://theforeman.org/api/1.16/apidoc/v2/ptables/index.html)  | List all partition tables |
| ptables_operatingsystems_index | [GET /api/ptables/:ptable_id/operatingsystems](https://theforeman.org/api/1.16/apidoc/v2/operatingsystems/index.html)  | List all operating systems for nested partition table |
| ptables_revision | [GET /api/ptables/revision](https://theforeman.org/api/1.16/apidoc/v2/ptables/revision.html)  |  |
| ptables_show | [GET /api/ptables/:id](https://theforeman.org/api/1.16/apidoc/v2/ptables/show.html)  | Show a partition table |
| ptables_update | [PUT /api/ptables/:id](https://theforeman.org/api/1.16/apidoc/v2/ptables/update.html)  | Update a partition table |
| puppet_modules_index | [GET /katello/api/puppet_modules](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/puppet_modules/index.html)  | List puppet_modules |
| puppet_modules_show | [GET /katello/api/puppet_modules/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/puppet_modules/show.html)  | Show a puppet module |
| puppetclasses_create | [POST /api/puppetclasses](https://theforeman.org/api/1.16/apidoc/v2/puppetclasses/create.html)  | Create a Puppet class |
| puppetclasses_destroy | [DELETE /api/puppetclasses/:id](https://theforeman.org/api/1.16/apidoc/v2/puppetclasses/destroy.html)  | Delete a Puppet class |
| puppetclasses_environments_index | [GET /api/puppetclasses/:puppetclass_id/environments](https://theforeman.org/api/1.16/apidoc/v2/environments/index.html)  | List environments of Puppet class |
| puppetclasses_hostgroups_index | [GET /api/puppetclasses/:puppetclass_id/hostgroups](https://theforeman.org/api/1.16/apidoc/v2/hostgroups/index.html)  | List all host groups for a Puppet class |
| puppetclasses_index | [GET /api/puppetclasses](https://theforeman.org/api/1.16/apidoc/v2/puppetclasses/index.html)  | List all Puppet classes |
| puppetclasses_show | [GET /api/puppetclasses/:id](https://theforeman.org/api/1.16/apidoc/v2/puppetclasses/show.html)  | Show a Puppet class |
| puppetclasses_smart_class_parameters_index | [GET /api/puppetclasses/:puppetclass_id/smart_class_parameters](https://theforeman.org/api/1.16/apidoc/v2/smart_class_parameters/index.html)  | List of smart class parameters for a specific Puppet class |
| puppetclasses_smart_variables_index | [GET /api/puppetclasses/:puppetclass_id/smart_variables](https://theforeman.org/api/1.16/apidoc/v2/smart_variables/index.html)  | List of smart variables for a specific Puppet class |
| puppetclasses_update | [PUT /api/puppetclasses/:id](https://theforeman.org/api/1.16/apidoc/v2/puppetclasses/update.html)  | Update a Puppet class |
| realms_create | [POST /api/realms](https://theforeman.org/api/1.16/apidoc/v2/realms/create.html)  | Create a realm |
| realms_destroy | [DELETE /api/realms/:id](https://theforeman.org/api/1.16/apidoc/v2/realms/destroy.html)  | Delete a realm |
| realms_index | [GET /api/realms](https://theforeman.org/api/1.16/apidoc/v2/realms/index.html)  | List of realms |
| realms_show | [GET /api/realms/:id](https://theforeman.org/api/1.16/apidoc/v2/realms/show.html)  | Show a realm |
| realms_update | [PUT /api/realms/:id](https://theforeman.org/api/1.16/apidoc/v2/realms/update.html)  | Update a realm |
| remote_execution_features_index | [GET /api/remote_execution_features](https://theforeman.org/api/1.16/apidoc/v2/remote_execution_features/index.html)  | List remote execution features |
| remote_execution_features_show | [GET /api/remote_execution_features/:id](https://theforeman.org/api/1.16/apidoc/v2/remote_execution_features/show.html)  | Show remote execution feature |
| remote_execution_features_update | [PUT /api/remote_execution_features/:id](https://theforeman.org/api/1.16/apidoc/v2/remote_execution_features/update.html)  | Update a job template |
| reports_create | [POST /api/reports](https://theforeman.org/api/1.16/apidoc/v2/reports/create.html)  | Create a report |
| reports_destroy | [DELETE /api/reports/:id](https://theforeman.org/api/1.16/apidoc/v2/reports/destroy.html)  | Delete a report |
| reports_index | [GET /api/reports](https://theforeman.org/api/1.16/apidoc/v2/reports/index.html)  | List all reports |
| reports_show | [GET /api/reports/:id](https://theforeman.org/api/1.16/apidoc/v2/reports/show.html)  | Show a report |
| repositories_content_uploads_create | [POST /katello/api/repositories/:repository_id/content_uploads](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_uploads/create.html)  | Create an upload request |
| repositories_content_uploads_epositories | [PUT /katello/api/repositories/:repository_id/content_uploads/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/content_uploads/update.html)  | Upload a chunk of the file's content |
| repositories_create | [POST /katello/api/repositories](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/create.html)  | Create a custom repository |
| repositories_destroy | [DELETE /katello/api/repositories/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/destroy.html)  | Destroy a custom repository |
| repositories_docker_manifests_epositories | [GET /katello/api/repositories/:repository_id/docker_manifests/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_manifests/show.html)  | Show a docker manifest |
| repositories_docker_manifests_index | [GET /katello/api/repositories/:repository_id/docker_manifests](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_manifests/index.html)  | List docker_manifests |
| repositories_docker_tags_epositories | [GET /katello/api/repositories/:repository_id/docker_tags/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_tags/show.html)  | Show a docker tag |
| repositories_docker_tags_index | [GET /katello/api/repositories/:repository_id/docker_tags](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/docker_tags/index.html)  | List docker_tags |
| repositories_errata_epositories | [GET /katello/api/repositories/:repository_id/errata/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/errata/show.html)  | Show an erratum |
| repositories_export | [POST /katello/api/repositories/:id/export](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/export.html)  | Export a repository |
| repositories_gpg_key_content | [GET /katello/api/repositories/:id/gpg_key_content](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/gpg_key_content.html)  | Return the content of a repo gpg key, used directly by yum |
| repositories_import_uploads | [PUT /katello/api/repositories/:id/import_uploads](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/import_uploads.html)  | Import uploads into a repository |
| repositories_index | [GET /katello/api/repositories](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/index.html)  | List of enabled repositories |
| repositories_ostree_branches_epositories | [GET /katello/api/repositories/:repository_id/ostree_branches/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/ostree_branches/show.html)  | Show an ostree branch |
| repositories_ostree_branches_index | [GET /katello/api/repositories/:repository_id/ostree_branches](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/ostree_branches/index.html)  | List ostree_branches |
| repositories_package_groups_epositories | [GET /katello/api/repositories/:repository_id/package_groups/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/package_groups/show.html)  | Show a package group |
| repositories_package_groups_index | [GET /katello/api/repositories/:repository_id/package_groups](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/package_groups/index.html)  | List package_groups |
| repositories_packages_epositories | [GET /katello/api/repositories/:repository_id/packages/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/packages/show.html)  | Show a package |
| repositories_packages_index | [GET /katello/api/repositories/:repository_id/packages](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/packages/index.html)  | List packages |
| repositories_puppet_modules_epositories | [GET /katello/api/repositories/:repository_id/puppet_modules/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/puppet_modules/show.html)  | Show a puppet module |
| repositories_puppet_modules_index | [GET /katello/api/repositories/:repository_id/puppet_modules](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/puppet_modules/index.html)  | List puppet_modules |
| repositories_remove_content | [PUT /katello/api/repositories/:id/remove_packages](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/remove_content.html)  |  |
| repositories_repositories_bulk_actions_destroy_repositories | [PUT /katello/api/repositories/bulk/destroy](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories_bulk_actions/destroy_repositories.html)  | Destroy one or more repositories |
| repositories_repositories_bulk_actions_sync_repositories | [POST /katello/api/repositories/bulk/sync](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories_bulk_actions/sync_repositories.html)  | Synchronize repository |
| repositories_repository_types | [GET /katello/api/repositories/repository_types](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/repository_types.html)  | Show the available repository types |
| repositories_republish | [PUT /katello/api/repositories/:id/republish](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/republish.html)  | Forces a republish of the specified repository, regenerating metadata and symlinks on the filesystem. |
| repositories_show | [GET /katello/api/repositories/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/show.html)  | Show a repository |
| repositories_sync | [POST /katello/api/repositories/:id/sync](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/sync.html)  | Sync a repository |
| repositories_sync_complete | [POST /katello/api/repositories/sync_complete](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/sync_complete.html)  |  |
| repositories_sync_index | [GET /katello/api/repositories/:repository_id/sync](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/sync/index.html)  | Get status of synchronisation for given repository |
| repositories_update | [PUT /katello/api/repositories/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/update.html)  | Update a repository |
| repositories_upload_content | [POST /katello/api/repositories/:id/upload_content](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/repositories/upload_content.html)  | Upload content into the repository |
| roles_create | [POST /api/roles](https://theforeman.org/api/1.16/apidoc/v2/roles/create.html)  | Create a role |
| roles_destroy | [DELETE /api/roles/:id](https://theforeman.org/api/1.16/apidoc/v2/roles/destroy.html)  | Delete a role |
| roles_index | [GET /api/roles](https://theforeman.org/api/1.16/apidoc/v2/roles/index.html)  | List all roles |
| roles_show | [GET /api/roles/:id](https://theforeman.org/api/1.16/apidoc/v2/roles/show.html)  | Show a role |
| roles_update | [PUT /api/roles/:id](https://theforeman.org/api/1.16/apidoc/v2/roles/update.html)  | Update a role |
| roles_users_index | [GET /api/roles/:role_id/users](https://theforeman.org/api/1.16/apidoc/v2/users/index.html)  | List all users for role |
| settings_index | [GET /api/settings](https://theforeman.org/api/1.16/apidoc/v2/settings/index.html)  | List all settings |
| settings_show | [GET /api/settings/:id](https://theforeman.org/api/1.16/apidoc/v2/settings/show.html)  | Show a setting |
| settings_update | [PUT /api/settings/:id](https://theforeman.org/api/1.16/apidoc/v2/settings/update.html)  | Update a setting |
| smart_class_parameters_index | [GET /api/smart_class_parameters](https://theforeman.org/api/1.16/apidoc/v2/smart_class_parameters/index.html)  | List all smart class parameters |
| smart_class_parameters_override_values_create | [POST /api/smart_class_parameters/:smart_class_parameter_id/override_values](https://theforeman.org/api/1.16/apidoc/v2/override_values/create.html)  | Create an override value for a specific smart class parameter |
| smart_class_parameters_override_values_index | [GET /api/smart_class_parameters/:smart_class_parameter_id/override_values](https://theforeman.org/api/1.16/apidoc/v2/override_values/index.html)  | List of override values for a specific smart class parameter |
| smart_class_parameters_override_values_smart_class_parameter_id_override_destroyvalues | [DELETE /api/smart_class_parameters/:smart_class_parameter_id/override_values/:id](https://theforeman.org/api/1.16/apidoc/v2/override_values/destroy.html)  | Delete an override value for a specific smart class parameter |
| smart_class_parameters_override_values_smart_class_parameter_id_override_showvalues | [GET /api/smart_class_parameters/:smart_class_parameter_id/override_values/:id](https://theforeman.org/api/1.16/apidoc/v2/override_values/show.html)  | Show an override value for a specific smart class parameter |
| smart_class_parameters_override_values_smart_class_parameter_id_override_updatevalues | [PUT /api/smart_class_parameters/:smart_class_parameter_id/override_values/:id](https://theforeman.org/api/1.16/apidoc/v2/override_values/update.html)  | Update an override value for a specific smart class parameter |
| smart_class_parameters_show | [GET /api/smart_class_parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/smart_class_parameters/show.html)  | Show a smart class parameter |
| smart_class_parameters_update | [PUT /api/smart_class_parameters/:id](https://theforeman.org/api/1.16/apidoc/v2/smart_class_parameters/update.html)  | Update a smart class parameter |
| smart_proxies_autosign_index | [GET /api/smart_proxies/smart_proxy_id/autosign](https://theforeman.org/api/1.16/apidoc/v2/autosign/index.html)  | List all autosign entries |
| smart_proxies_create | [POST /api/smart_proxies](https://theforeman.org/api/1.16/apidoc/v2/smart_proxies/create.html)  | Create a capsule |
| smart_proxies_destroy | [DELETE /api/smart_proxies/:id](https://theforeman.org/api/1.16/apidoc/v2/smart_proxies/destroy.html)  | Delete a capsule |
| smart_proxies_environments_import_puppetclasses | [POST /api/smart_proxies/:id/import_puppetclasses](https://theforeman.org/api/1.16/apidoc/v2/environments/import_puppetclasses.html)  | Import puppet classes from puppet Capsule. |
| smart_proxies_environments_smart_proxy_id_import_puppetclassesenvironments | [POST /api/smart_proxies/:smart_proxy_id/environments/:id/import_puppetclasses](https://theforeman.org/api/1.16/apidoc/v2/environments/import_puppetclasses.html)  | Import puppet classes from puppet Capsule for an environment |
| smart_proxies_import_puppetclasses | [POST /api/smart_proxies/:id/import_puppetclasses](https://theforeman.org/api/1.16/apidoc/v2/smart_proxies/import_puppetclasses.html)  | Import puppet classes from puppet Capsule. |
| smart_proxies_index | [GET /api/smart_proxies](https://theforeman.org/api/1.16/apidoc/v2/smart_proxies/index.html)  | List all capsules |
| smart_proxies_refresh | [PUT /api/smart_proxies/:id/refresh](https://theforeman.org/api/1.16/apidoc/v2/smart_proxies/refresh.html)  | Refresh capsule features |
| smart_proxies_show | [GET /api/smart_proxies/:id](https://theforeman.org/api/1.16/apidoc/v2/smart_proxies/show.html)  | Show a capsule |
| smart_proxies_smart_proxy_id_import_puppetclassesenvironments | [POST /api/smart_proxies/:smart_proxy_id/environments/:id/import_puppetclasses](https://theforeman.org/api/1.16/apidoc/v2/smart_proxies/import_puppetclasses.html)  | Import puppet classes from puppet Capsule for an environment |
| smart_proxies_update | [PUT /api/smart_proxies/:id](https://theforeman.org/api/1.16/apidoc/v2/smart_proxies/update.html)  | Update a capsule |
| smart_variables_create | [POST /api/smart_variables](https://theforeman.org/api/1.16/apidoc/v2/smart_variables/create.html)  | Create a smart variable |
| smart_variables_destroy | [DELETE /api/smart_variables/:id](https://theforeman.org/api/1.16/apidoc/v2/smart_variables/destroy.html)  | Delete a smart variable |
| smart_variables_index | [GET /api/smart_variables](https://theforeman.org/api/1.16/apidoc/v2/smart_variables/index.html)  | List all smart variables |
| smart_variables_override_values_create | [POST /api/smart_variables/:smart_variable_id/override_values](https://theforeman.org/api/1.16/apidoc/v2/override_values/create.html)  | Create an override value for a specific smart variable |
| smart_variables_override_values_index | [GET /api/smart_variables/:smart_variable_id/override_values](https://theforeman.org/api/1.16/apidoc/v2/override_values/index.html)  | List of override values for a specific smart variable |
| smart_variables_override_values_smart_variable_id_override_destroyvalues | [DELETE /api/smart_variables/:smart_variable_id/override_values/:id](https://theforeman.org/api/1.16/apidoc/v2/override_values/destroy.html)  | Delete an override value for a specific smart variable |
| smart_variables_override_values_smart_variable_id_override_showvalues | [GET /api/smart_variables/:smart_variable_id/override_values/:id](https://theforeman.org/api/1.16/apidoc/v2/override_values/show.html)  | Show an override value for a specific smart variable |
| smart_variables_override_values_smart_variable_id_override_updatevalues | [PUT /api/smart_variables/:smart_variable_id/override_values/:id](https://theforeman.org/api/1.16/apidoc/v2/override_values/update.html)  | Update an override value for a specific smart variable |
| smart_variables_show | [GET /api/smart_variables/:id](https://theforeman.org/api/1.16/apidoc/v2/smart_variables/show.html)  | Show a smart variable |
| smart_variables_update | [PUT /api/smart_variables/:id](https://theforeman.org/api/1.16/apidoc/v2/smart_variables/update.html)  | Update a smart variable |
| statistics_index | [GET /api/statistics](https://theforeman.org/api/1.16/apidoc/v2/statistics/index.html)  | Get statistics |
| status_home_status | [GET /api/status](https://theforeman.org/api/1.16/apidoc/v2/home/status.html)  | Show status |
| status_ping_server_status | [GET /katello/api/status](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/ping/server_status.html)  | Shows version information |
| subnets_create | [POST /api/subnets](https://theforeman.org/api/1.16/apidoc/v2/subnets/create.html)  | Create a subnet |
| subnets_destroy | [DELETE /api/subnets/:id](https://theforeman.org/api/1.16/apidoc/v2/subnets/destroy.html)  | Delete a subnet |
| subnets_domains_index | [GET /api/subnets/:subnet_id/domains](https://theforeman.org/api/1.16/apidoc/v2/domains/index.html)  | List of domains per subnet |
| subnets_index | [GET /api/subnets](https://theforeman.org/api/1.16/apidoc/v2/subnets/index.html)  | List of subnets |
| subnets_interfaces_index | [GET /api/subnets/:subnet_id/interfaces](https://theforeman.org/api/1.16/apidoc/v2/interfaces/index.html)  | List all interfaces for subnet |
| subnets_show | [GET /api/subnets/:id](https://theforeman.org/api/1.16/apidoc/v2/subnets/show.html)  | Show a subnet |
| subnets_update | [PUT /api/subnets/:id](https://theforeman.org/api/1.16/apidoc/v2/subnets/update.html)  | Update a subnet |
| subscriptions_index | [GET /katello/api/subscriptions](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/subscriptions/index.html)  |  |
| subscriptions_products_index | [GET /katello/api/subscriptions/:subscription_id/products](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/products/index.html)  | List of subscription products in a subscription |
| subscriptions_show | [GET /katello/api/subscriptions/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/subscriptions/show.html)  | Show a subscription |
| sync_plans_destroy | [DELETE /katello/api/sync_plans/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/sync_plans/destroy.html)  | Destroy a sync plan |
| sync_plans_index | [GET /katello/api/sync_plans](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/sync_plans/index.html)  | List sync plans |
| sync_plans_products_index | [GET /katello/api/sync_plans/:sync_plan_id/products](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/products/index.html)  | List of Products for sync plan |
| sync_plans_show | [GET /katello/api/sync_plans/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/sync_plans/show.html)  | Show a sync plan |
| sync_plans_sync | [PUT /katello/api/sync_plans/:id/sync](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/sync_plans/sync.html)  | Initiate a sync of the products attached to the sync plan |
| sync_plans_update | [PUT /katello/api/sync_plans/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/sync_plans/update.html)  | Update a sync plan |
| systems_index | [GET /katello/api/systems](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/systems/index.html)  | List content hosts |
| systems_releases | [GET /katello/api/systems/:id/releases](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/systems/releases.html)  | Show releases available for the content host |
| systems_show | [GET /katello/api/systems/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/systems/show.html)  | Show a content host |
| systems_update | [PUT /katello/api/systems/:id](https://theforeman.org/plugins/katello/3.4/api/apidoc/v2/systems/update.html)  | Update content host information |
| template_combinations_destroy | [DELETE /api/template_combinations/:id](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/destroy.html)  | Delete a template combination |
| template_combinations_show | [GET /api/template_combinations/:id](https://theforeman.org/api/1.16/apidoc/v2/template_combinations/show.html)  | Show template combination |
| template_kinds_index | [GET /api/template_kinds](https://theforeman.org/api/1.16/apidoc/v2/template_kinds/index.html)  | List all template kinds |
| templates_foreign_input_sets_create | [POST /api/templates/:template_id/foreign_input_sets](https://theforeman.org/api/1.16/apidoc/v2/foreign_input_sets/create.html)  | Create a foreign input set |
| templates_foreign_input_sets_index | [GET /api/templates/:template_id/foreign_input_sets](https://theforeman.org/api/1.16/apidoc/v2/foreign_input_sets/index.html)  | List foreign input sets |
| templates_foreign_input_sets_template_id_foreign_input_destroysets | [DELETE /api/templates/:template_id/foreign_input_sets/:id](https://theforeman.org/api/1.16/apidoc/v2/foreign_input_sets/destroy.html)  | Delete a foreign input set |
| templates_foreign_input_sets_template_id_foreign_input_showsets | [GET /api/templates/:template_id/foreign_input_sets/:id](https://theforeman.org/api/1.16/apidoc/v2/foreign_input_sets/show.html)  | Show foreign input set details |
| templates_foreign_input_sets_template_id_foreign_input_updatesets | [PUT /api/templates/:template_id/foreign_input_sets/:id](https://theforeman.org/api/1.16/apidoc/v2/foreign_input_sets/update.html)  | Update a foreign input set |
| templates_template_inputs_create | [POST /api/templates/:template_id/template_inputs](https://theforeman.org/api/1.16/apidoc/v2/template_inputs/create.html)  | Create a template input |
| templates_template_inputs_index | [GET /api/templates/:template_id/template_inputs](https://theforeman.org/api/1.16/apidoc/v2/template_inputs/index.html)  | List template inputs |
| templates_template_inputs_template_id_template_destroyinputs | [DELETE /api/templates/:template_id/template_inputs/:id](https://theforeman.org/api/1.16/apidoc/v2/template_inputs/destroy.html)  | Delete a template input |
| templates_template_inputs_template_id_template_showinputs | [GET /api/templates/:template_id/template_inputs/:id](https://theforeman.org/api/1.16/apidoc/v2/template_inputs/show.html)  | Show template input details |
| templates_template_inputs_template_id_template_updateinputs | [PUT /api/templates/:template_id/template_inputs/:id](https://theforeman.org/api/1.16/apidoc/v2/template_inputs/update.html)  | Update a template input |
| usergroups_create | [POST /api/usergroups](https://theforeman.org/api/1.16/apidoc/v2/usergroups/create.html)  | Create a user group |
| usergroups_destroy | [DELETE /api/usergroups/:id](https://theforeman.org/api/1.16/apidoc/v2/usergroups/destroy.html)  | Delete a user group |
| usergroups_external_usergroups_create | [POST /api/usergroups/:usergroup_id/external_usergroups](https://theforeman.org/api/1.16/apidoc/v2/external_usergroups/create.html)  | Create an external user group linked to a user group |
| usergroups_external_usergroups_index | [GET /api/usergroups/:usergroup_id/external_usergroups](https://theforeman.org/api/1.16/apidoc/v2/external_usergroups/index.html)  | List all external user groups for user group |
| usergroups_external_usergroups_usergroup_id_external_destroyusergroups | [DELETE /api/usergroups/:usergroup_id/external_usergroups/:id](https://theforeman.org/api/1.16/apidoc/v2/external_usergroups/destroy.html)  | Delete an external user group |
| usergroups_external_usergroups_usergroup_id_external_refreshusergroups | [PUT /api/usergroups/:usergroup_id/external_usergroups/:id/refresh](https://theforeman.org/api/1.16/apidoc/v2/external_usergroups/refresh.html)  | Refresh external user group |
| usergroups_external_usergroups_usergroup_id_external_showusergroups | [GET /api/usergroups/:usergroup_id/external_usergroups/:id](https://theforeman.org/api/1.16/apidoc/v2/external_usergroups/show.html)  | Show an external user group for user group |
| usergroups_external_usergroups_usergroup_id_external_updateusergroups | [PUT /api/usergroups/:usergroup_id/external_usergroups/:id](https://theforeman.org/api/1.16/apidoc/v2/external_usergroups/update.html)  | Update external user group |
| usergroups_index | [GET /api/usergroups](https://theforeman.org/api/1.16/apidoc/v2/usergroups/index.html)  | List all user groups |
| usergroups_show | [GET /api/usergroups/:id](https://theforeman.org/api/1.16/apidoc/v2/usergroups/show.html)  | Show a user group |
| usergroups_update | [PUT /api/usergroups/:id](https://theforeman.org/api/1.16/apidoc/v2/usergroups/update.html)  | Update a user group |
| usergroups_users_index | [GET /api/usergroups/:usergroup_id/users](https://theforeman.org/api/1.16/apidoc/v2/users/index.html)  | List all users for user group |
| users_create | [POST /api/users](https://theforeman.org/api/1.16/apidoc/v2/users/create.html)  | Create a user |
| users_destroy | [DELETE /api/users/:id](https://theforeman.org/api/1.16/apidoc/v2/users/destroy.html)  | Delete a user |
| users_index | [GET /api/users](https://theforeman.org/api/1.16/apidoc/v2/users/index.html)  | List all users |
| users_show | [GET /api/users/:id](https://theforeman.org/api/1.16/apidoc/v2/users/show.html)  | Show a user |
| users_update | [PUT /api/users/:id](https://theforeman.org/api/1.16/apidoc/v2/users/update.html)  | Update a user |