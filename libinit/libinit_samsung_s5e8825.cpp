/*
 * Copyright (C) The LineageOS Project
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <libinit_variant.h>

#include "vendor_init.h"

static const variant_info_t unknown = {
    .device = "unknown",
    .model = "unknown",
    .name = "unknown",
    .build_fingerprint = "unknown",
    .build_desc = "unknown"
};

static const variant_info_t a53xdcm = {
    .device = "a53x",
    .model = "SC-53C",
    .name = "a53xdcm",
    .build_fingerprint = "samsung/a53xdcm/essi:15/AP3A.240905.015.A2/SC53COMU1DYF2:user/release-keys",
    .build_desc = "a53xdcm-user 15 AP3A.240905.015.A2 SC53COMU1DYF2 release-keys"
};

static const variant_info_t a53xksx = {
    .device = "a53x",
    .model = "SM-A536N",
    .name = "a53xksx",
    .build_fingerprint = "samsung/a53xksx/essi:15/AP3A.240905.015.A2/A536NKSSCFYH1:user/release-keys",
    .build_desc = "a53xksx-user 15 AP3A.240905.015.A2 A536NKSSCFYH1 release-keys"
};

static const variant_info_t a53xnaxx = {
    .device = "a53x",
    .model = "SM-A536B",
    .name = "a53xnaxx",
    .build_fingerprint = "samsung/a53xnaxx/essi:15/AP3A.240905.015.A2/A536BXXSHFYH1:user/release-keys",
    .build_desc = "a53xnaxx-user 15 AP3A.240905.015.A2 A536BXXSHFYH1 release-keys"
};

static const variant_info_t a53xnsxx = {
    .device = "a53x",
    .model = "SM-A536E",
    .name = "a53xnsxx",
    .build_fingerprint = "samsung/a53xnsxx/essi:15/AP3A.240905.015.A2/A536EXXSHFYH2:user/release-keys",
    .build_desc = "a53xnsxx-user 15 AP3A.240905.015.A2 A536EXXSHFYH2 release-keys"
};

static const variant_info_t a53xzc = {
    .device = "a53x",
    .model = "SM-A5360",
    .name = "a53xzc",
    .build_fingerprint = "samsung/a53xzc/essi:15/AP3A.240905.015.A2/A5360ZCSHFYH1:user/release-keys",
    .build_desc = "a53xzc-user 15 AP3A.240905.015.A2 A5360ZCSHFYH1 release-keys"
};

static const std::vector<variant_info_t> variants = {
    a53xdcm,
    a53xksx,
    a53xnaxx,
    a53xnsxx,
    a53xzc,
    unknown,
};

void vendor_load_properties() {
    search_variant(variants);
}
