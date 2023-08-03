from sentence_transformers import CrossEncoder

model = CrossEncoder("cross-encoder/mmarco-mMiniLMv2-L12-H384-v1")
scores = model.predict(
    [
        (
            "Why Deep Fried Foods May Cause Cancer",
            "Background Evidence suggests that high-heat cooking methods may increase the risk of prostate cancer (PCa). The addition of oil/fat, as in deep-frying, may be of particular concern, and has not specifically been investigated in relation to PCa. Potential mechanisms include the formation of potentially carcinogenic agents such as aldehydes, acrolein, heterocyclic amines, polycyclic aromatic hydrocarbons, and acrylamide. Methods We estimated odds ratios (OR) and 95% confidence intervals (CI) for the association between tertiles of intake of deep-fried foods from a food frequency questionnaire (French fries, fried chicken, fried fish, doughnuts and snack chips) and PCa risk, adjusted for potential confounders, among 1,549 cases and 1,492 controls. We additionally examined associations with more aggressive PCa (defined as regional/distant stage, elevated Gleason score or prostate specific antigen level). Results Compared with <1/week, there was a positive association with PCa risk for intake \u2265 1/week of French fries (OR=1.37; 95% CI, 1.11\u20131.69), fried chicken (OR=1.30; 95% CI, 1.04\u20131.62), fried fish (OR=1.32; 95% CI, 1.05\u20131.66), and doughnuts (OR=1.35; 95% CI, 1.11\u20131.66). There was no association for snack chips (OR=1.08; 95% CI, 0.89\u20131.32). Most of the estimates were slightly stronger for more aggressive disease (OR=1.41; 95% CI, 1.04\u20131.92 for fried fish). Conclusion Regular consumption of select deep-fried foods is associated with increased PCa risk. Whether this risk is specific to deep-fried foods, or whether it represents risk associated with regular intake of foods exposed to high heat and/or other aspects of the Western lifestyle, such as fast food consumption, remains to be determined.",
        ),
        (
            "Why Deep Fried Foods May Cause Cancer",
            "Background: Meat, milk, and eggs have been inconsistently associated with the risk of advanced prostate cancer. These foods are sources of choline\u2014a nutrient that may affect prostate cancer progression through cell membrane function and one-carbon metabolism. No study has examined dietary choline and the risk of lethal prostate cancer. Objective: Our objective was to examine whether dietary choline, choline-containing compounds, and betaine (a choline metabolite) increase the risk of lethal prostate cancer. Design: We prospectively examined the intake of these nutrients and the risk of lethal prostate cancer among 47,896 men in the Health Professionals Follow-Up Study. In a case-only survival analysis, we examined the postdiagnostic intake of these nutrients and the risk of lethal prostate cancer among 4282 men with an initial diagnosis of nonmetastatic disease during follow-up. Diet was assessed with a validated questionnaire 6 times during 22 y of follow-up. Results: In the incidence analysis, we observed 695 lethal prostate cancers during 879,627 person-years. Men in the highest quintile of choline intake had a 70% increased risk of lethal prostate cancer (HR: 1.70; 95% CI: 1.18, 2.45; P-trend = 0.005). In the case-only survival analysis, we observed 271 lethal cases during 33,679 person-years. Postdiagnostic choline intake was not statistically significantly associated with the risk of lethal prostate cancer (HR for quintile 5 compared with quintile 1: 1.69; 95% CI: 0.93, 3.09; P-trend = 0.20). Conclusion: Of the 47,896 men in our study population, choline intake was associated with an increased risk of lethal prostate cancer.:w"
            "",
        ),
        (
            "Why Deep Fried Foods May Cause Cancer",
            "Environmental factors such as diets rich in saturated fats contribute to dysfunction and death of pancreatic \u03b2-cells in diabetes. Endoplasmic reticulum (ER) stress is elicited in \u03b2-cells by saturated fatty acids. Here we show that palmitate-induced \u03b2-cell apoptosis is mediated by the intrinsic mitochondrial pathway. By microarray analysis, we identified a palmitate-triggered ER stress gene expression signature and the induction of the BH3-only proteins death protein 5 (DP5) and p53-upregulated modulator of apoptosis (PUMA). Knockdown of either protein reduced cytochrome c release, caspase-3 activation, and apoptosis in rat and human \u03b2-cells. DP5 induction depends on inositol-requiring enzyme 1 (IRE1)\u2013dependent c-Jun NH2-terminal kinase and PKR\u2013like ER kinase (PERK)\u2013induced activating transcription factor (ATF3) binding to its promoter. PUMA expression is also PERK/ATF3-dependent, through tribbles 3 (TRB3)\u2013regulated AKT inhibition and FoxO3a activation. DP5\u2212/\u2212 mice are protected from high fat diet\u2013induced loss of glucose tolerance and have twofold greater pancreatic \u03b2-cell mass. This study elucidates the crosstalk between lipotoxic ER stress and the mitochondrial pathway of apoptosis that causes \u03b2-cell death in diabetes.",
        ),
    ]
)
print(scores)
