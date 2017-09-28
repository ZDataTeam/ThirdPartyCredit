package com.allinpay.common.certification.util;

import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import com.antgroup.zmxy.openplatform.api.internal.util.StringUtils;
import com.google.common.collect.Lists;
import com.google.common.collect.Maps;

public class AliCerticationCodeUtil {

	/************************** 欺诈信息code解析 ***********************************/
	private static Map<String, String> codeMap = Maps.newHashMap();
	private static Map<String, String> resourceCodeMap = Maps.newHashMap();
	private static Map<String, String> targetCodeMap = Maps.newHashMap();
	private static Map<String, String> matchCodeMap = Maps.newHashMap();

	// 2种类型时间段的使用情况
	private static Map<String, String> validateCodeMapPhone = Maps.newHashMap();
	private static Map<String, String> validateCodeMap = Maps.newHashMap();

	/************************** 欺诈关注清单code解析 ***********************************/

	private static Map<String, String> riskCodesMap = Maps.newHashMap();

	static {
		// NA,UM,UK
		/************************** 欺诈信息map ***********************************/
		// 补充的规则
		codeMap.put("V_AD_CN_MA_WORK", "地址与本人工作地匹配");
		codeMap.put("V_AD_CN_MA_HOME", "地址与本人居住地匹配");

		// 配置项1
		resourceCodeMap.put("CN", "身份证号");
		resourceCodeMap.put("NM", "姓名");
		resourceCodeMap.put("PH", "手机号码");
		resourceCodeMap.put("BC", "银行号码");
		resourceCodeMap.put("AD", "地址");
		resourceCodeMap.put("EM", "邮箱");
		resourceCodeMap.put("IP", "IP");
		resourceCodeMap.put("MC", "MAC");
		resourceCodeMap.put("WF", "WIFI-MAC");
		resourceCodeMap.put("IM", "IMEI");

		// 配置项2
		targetCodeMap.put("CN", "本人");
		targetCodeMap.put("PH", "手机号码");
		targetCodeMap.put("NM", "姓名");

		// 配置结果
		matchCodeMap.put("MA", "信息匹配");
		matchCodeMap.put("UM", "信息不匹配");
		matchCodeMap.put("UK", "信息匹配未知");

		// 结果详情
		validateCodeMapPhone.put("UL30D", "30天内有使用");
		validateCodeMapPhone.put("UL90D", "距今[30,90)天内有使用");
		validateCodeMapPhone.put("UL180D", "距今[90,180)天内有使用");
		validateCodeMapPhone.put("UM180D", "180天内没有使用");

		validateCodeMap.put("UL180D", "180天内有使用");
		validateCodeMap.put("UL360D", "距今[180,360)天内有使用");
		validateCodeMap.put("UM360D", "360天内没有使用");

		/************************** 欺诈关注清单map ***********************************/

		riskCodesMap.put("R_CN_001", "身份证号击中网络欺诈风险名单[中风险]");
		riskCodesMap.put("R_CN_002", "身份证号曾经被泄露[低风险]");
		riskCodesMap.put("R_CN_003", "身份证号曾经被冒用[低风险]");
		riskCodesMap.put("R_CN_004", "身份证号出现在风险关联网络[低风险]");
		riskCodesMap.put("R_CN_JJ_01", "身份证当天在多个商户申请[中风险]");
		riskCodesMap.put("R_CN_JJ_02", "身份证近一周(不包括当天)在多个商户申请[中风险]");
		riskCodesMap.put("R_CN_JJ_03", "身份证近一月(不包括当天)在多个商户申请[中风险]");

		riskCodesMap.put("R_PH_001", "手机号击中网络欺诈风险名单[中风险]");
		riskCodesMap.put("R_PH_002", "手机号疑似多个用户共用[低风险]");
		riskCodesMap.put("R_PH_003", "手机号疑似虚拟运营商小号[中风险]");
		riskCodesMap.put("R_PH_004", "手机号疑似二次放号[高风险]");
		riskCodesMap.put("R_PH_005", "手机号失联风险高[高风险]");
		riskCodesMap.put("R_PH_006", "手机号稳定性弱[低风险]");
		riskCodesMap.put("R_PH_JJ_01", "手机号当天在多个商户申请[中风险]");
		riskCodesMap.put("R_PH_JJ_02", "手机号近一周(不包括当天)在多个商户申请[中风险]");
		riskCodesMap.put("R_PH_JJ_03", "手机号近一月(不包括当天)在多个商户申请[中风险]");

		riskCodesMap.put("R_BC_001", "银行卡击中网络欺诈风险名单[中风险]");
		riskCodesMap.put("R_BC_002", "银行卡曾经被泄露[低风险]");
		riskCodesMap.put("R_BC_003", "银行卡曾经被冒用[低风险]");

		riskCodesMap.put("R_AD_001", "疑似虚假地址[低风险]");

		riskCodesMap.put("R_MC_001", "疑似篡改的MAC[中风险]");
		riskCodesMap.put("R_MC_002", "MAC击中网络欺诈风险名单[中风险]");
		riskCodesMap.put("R_MC_003", "手机MAC近期不活跃[低风险]");
		riskCodesMap.put("R_MC_004", "手机MAC较新[低风险]");
		riskCodesMap.put("R_MC_005", "恶意攻击MAC[中风险]");
		riskCodesMap.put("R_MC_006", "疑似中介MAC[中风险]");
		riskCodesMap.put("R_MC_JJ_01", "当天多个用户通过该MAC申请[中风险]");
		riskCodesMap.put("R_MC_JJ_02", "近一周(不包括当天)多个用户通过该MAC申请[中风险]");
		riskCodesMap.put("R_MC_JJ_03", "近一月(不包括当天)多个用户通过该MAC申请[中风险]");

		riskCodesMap.put("R_IP_001", "代理IP[中风险]");
		riskCodesMap.put("R_IP_002", "服务器IP[低风险]");
		riskCodesMap.put("R_IP_003", "热点IP[低风险]");
		riskCodesMap.put("R_IP_004", "IP近期不活跃[低风险]");
		riskCodesMap.put("R_IP_005", "IP较新[低风险]");
		riskCodesMap.put("R_IP_006", "IP上聚集多个设备[低风险]");
		riskCodesMap.put("R_IP_007", "IP上设备分布异常[低风险]");
		riskCodesMap.put("R_IP_008", "疑似中介IP[中风险]");
		riskCodesMap.put("R_IP_JJ_01", "当天多个用户通过该IP申请[中风险]");
		riskCodesMap.put("R_IP_JJ_02", "近一周(不包括当天)多个用户通过该IP申请[中风险]");
		riskCodesMap.put("R_IP_JJ_03", "近一月(不包括当天)多个用户通过该IP申请[中风险]");

		riskCodesMap.put("R_IM_001", "IMEI击中网络欺诈风险名单[中风险]");
		riskCodesMap.put("R_IM_002", "IMEI近期不活跃[低风险]");
		riskCodesMap.put("R_IM_003", "IMEI较新[低风险]");
		riskCodesMap.put("R_IM_004", "疑似虚假IMEI[中风险]");
		riskCodesMap.put("R_IM_JJ_01", "当天多个用户通过该IMEI申请[中风险]");
		riskCodesMap.put("R_IM_JJ_02", "近一周(不包括当天)多个用户通过该IMEI申请[中风险]");
		riskCodesMap.put("R_IM_JJ_03", "近一月(不包括当天)多个用户通过该IMEI申请[中风险]");

	}

	/**
	 * 解析 欺诈信息验证code
	 * 
	 * @param codeList
	 * @return
	 */
	public static String parseCodes(List<String> codeList) {
		StringBuilder message = new StringBuilder();
		if (codeList != null) {
			for (String code : codeList) {
				message.append(parseCode(code)).append(";");
			}
		}
		return message.toString();
	}

	/**
	 * 
	 * @param codeList
	 * @return
	 */
	public static boolean parseAcrossVerify(List<String> codeList) {
		boolean across = true;
		if (codeList != null) {
			for (String code : codeList) {
				if (!StringUtils.isEmpty(code)) {
					String[] codes = code.split("_");
					String lastCode = codes[codes.length - 1];
					// 只拦截NA、不匹配、未知  放行未使用
					if ("NA".equals(lastCode) || "UM".equals(lastCode) || "UK".equals(lastCode)) {
						across = false;
						break;
					}
				}
			}
		}
		return across;
	}

	public static String parseRiskCodes(List<String> codeList) {
		StringBuilder message = new StringBuilder();
		if (codeList != null) {
			for (String code : codeList) {
				message.append(riskCodesMap.get(code)).append(";");
			}
		}
		return message.toString();
	}

	/**
	 * like V_CN_NM_MA, V_PH_CN_MA_UM180D, V_BC_CN_UK
	 * 
	 * @param codeList
	 * @return
	 */
	public static String parseCode(String code) {
		// 默认
		String defaultMsg = codeMap.get(code);
		if (!StringUtils.isEmpty(defaultMsg))
			return defaultMsg;

		String[] codes = code.split("_");
		int size = codes.length;

		// 处理信息 like: "V_PH_NA" "查询不到电话号码信息"
		if (size == 3 && code.indexOf("NA") != -1) {
			String resourceDesc = resourceCodeMap.get(codes[1]);
			return "查询不到".concat(resourceDesc == null ? codes[1] : resourceDesc).concat("信息");
		}

		StringBuilder message = new StringBuilder();
		boolean validatePhone = false;
		if (size > 1) {
			if ("PH".equals(codes[1])) {
				validatePhone = true;
			}
			message.append(resourceCodeMap.get(codes[1]));
		}
		if (size > 2) {
			message.append("与").append(targetCodeMap.get(codes[2]));
		}
		if (size > 3) {
			message.append(matchCodeMap.get(codes[3]));
		}
		if (size > 4) {

			message.append(",").append(parseValidateResult(codes[4], validatePhone));
		}
		return message.toString();
	}

	private static String parseValidateResult(String code, boolean validatePhone) {
		String validateResult = validatePhone ? validateCodeMapPhone.get(code) : validateCodeMap.get(code);
		return StringUtils.isEmpty(validateResult) ? parseValidateResult(code) : validateResult;
	}

	private static String parseValidateResult(String code) {
		String regEx = "[^0-9]";
		Pattern p = Pattern.compile(regEx);
		try {
			Matcher m = p.matcher(code);
			return m.replaceAll("").trim().concat(code.indexOf("UL") != -1 ? "天内有使用" : "天内没有使用");
		} catch (Exception e) {
			return "";
		}

	}

	public static void main(String[] args) {
		// System.out.println(parseCodes(Lists.newArrayList("V_CN_NM_MA",
		// "V_AD_PH_MA_UM360D", "V_BC_CN_UK")));
		System.out.println(parseAcrossVerify(Lists.newArrayList("V_CN_NM_MA", "")));
	}

}
