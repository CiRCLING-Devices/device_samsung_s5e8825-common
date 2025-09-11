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

static const variant_info_t a25xdxx = {
    .device = "a25x",
    .model = "SM-A256E",
    .name = "a25xdxx",
    .build_fingerprint = "samsung/a25xdxx/essi:15/AP3A.240905.015.A2/A256EXXS8CYG3:user/release-keys",
    .build_desc = "a25xdxx-user 15 AP3A.240905.015.A2 A256EXXS8CYG3 release-keys"
};

static const variant_info_t a25xxx = {
    .device = "a25x",
    .model = "SM-A256B",
    .name = "a25xxx",
    .build_fingerprint = "samsung/a25xxx/essi:15/AP3A.240905.015.A2/A256BXXS8CYG4:user/release-keys",
    .build_desc = "a25xxx-user 15 AP3A.240905.015.A2 A256BXXS8CYG4 release-keys"
};

static const variant_info_t a25zhx = {
    .device = "a25x",
    .model = "SM-A2560",
    .name = "a25zhx",
    .build_fingerprint = "samsung/a25zhx/essi:15/AP3A.240905.015.A2/A2560ZHS7CYG4:user/release-keys",
    .build_desc = "a25zhx-user 15 AP3A.240905.015.A2 A2560ZHS7CYG4 release-keys"
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

static const variant_info_t m34xdxx = {
    .device = "m34x",
    .model = "SM-M346B1",
    .name = "m34xdxx",
    .build_fingerprint = "samsung/m34xdxx/essi:15/AP3A.240905.015.A2/M346B1DXS8DYH1:user/release-keys",
    .build_desc = "m34xdxx-user 15 AP3A.240905.015.A2 M346B1DXS8DYH1 release-keys"
};

static const variant_info_t m34xins = {
    .device = "m34x",
    .model = "SM-E346B",
    .name = "m34xins",
    .build_fingerprint = "samsung/m34xins/essi:15/AP3A.240905.015.A2/E346BXXS8DYH1:user/release-keys",
    .build_desc = "m34xins-user 15 AP3A.240905.015.A2 E346BXXS8DYH1 release-keys"
};

static const variant_info_t m34xjxx = {
    .device = "m34x",
    .model = "SM-M346B2",
    .name = "m34xjxx",
    .build_fingerprint = "samsung/m34xjxx/essi:15/AP3A.240905.015.A2/M346B2XUS8DYH1:user/release-keys",
    .build_desc = "m34xjxx-user 15 AP3A.240905.015.A2 M346B2XUS8DYH1 release-keys"
};

static const variant_info_t m34xnsxx = {
    .device = "m34x",
    .model = "SM-M346B",
    .name = "m34xnsxx",
    .build_fingerprint = "samsung/m34xnsxx/essi:15/AP3A.240905.015.A2/M346BXXS8DYH1:user/release-keys",
    .build_desc = "m34xnsxx-user 15 AP3A.240905.015.A2 M346BXXS8DYH1 release-keys"
};

static const std::vector<variant_info_t> variants = {
    a25xdxx,
    a25xxx,
    a25zhx,
    a53xdcm,
    a53xksx,
    a53xnaxx,
    a53xnsxx,
    a53xzc,
    m34xdxx,
    m34xins,
    m34xjxx,
    m34xnsxx,
    unknown,
};

void vendor_load_properties() {
    search_variant(variants);
}
